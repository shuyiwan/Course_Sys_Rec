from search import models
import ratemyprofessor

def fetch_all_professors() -> dict:
    """
    Query all classes from the database, and store all professor from each class
    """
    db_query = models.CachedCourses.objects.all()

    for class_object in db_query:
        each_class = class_object.data
        print("CourseID: " + each_class["courseId"])
        print("Title: " + each_class["title"]) 

        if each_class["classSections"] and each_class["classSections"][0]["instructors"]:
                raw_profname = each_class["classSections"][0]["instructors"][0]["instructor"]
        else:
            print("Skipped: " + "no instructor for " + each_class["courseId"])
            continue
        
        # get rid of the inital of the middle name, otherwise ratemyprofessor api could fail
        if raw_profname.count(" ") >= 1:
            profname = raw_profname.split(" ")[0] + " " + raw_profname.split(" ")[1]
        else:
            profname = raw_profname

        # if we already have professors with this name, we need to link the class to them
        existing_prof = models.Professor.objects.filter(name=profname)
        if existing_prof.exists():
            for each_prof in existing_prof:
                class_object.instructor = each_prof
                class_object.save()
            print("Skipped: " + f"{profname} is already stored" )
            continue
        
        # otherwise, we need to create a new professor
        fetch_professor_for_classes(class_object, profname)

    print("Success! Finished querying")

def fetch_professor_for_classes(each_class: models.CachedCourses, prof_name: str) -> None:
    """
    Query the professor from ratemyprofessor api, and store it in the database
    """
    SCHOOL = ratemyprofessor.get_school_by_name("University of California Santa Barbara")
    prof_list = ratemyprofessor.get_professors_by_school_and_name(SCHOOL, prof_name)

    if not prof_list:
        print(f"Skipped: {prof_name} not found in ratemyprofessor")
        return
    if prof_list[0].school.name != "University of California Santa Barbara":
        print(f"Skipped: there is no professor with name {prof_name} found in UCSB")
        return

    
    for prof_object in prof_list:
        if (prof_object.would_take_again is not None) and (prof_object.would_take_again != -1):
            would_take_again = str(round(prof_object.would_take_again))
        else:
            would_take_again = "N/A"
        new_prof = models.Professor(fullname = prof_object.name,
                                     name = prof_name,
                                     department = prof_object.department,
                                     rating = prof_object.rating,
                                     difficulty = prof_object.difficulty,
                                     num_ratings = prof_object.num_ratings,
                                     would_take_again = would_take_again)
        new_prof.save()
        each_class.instructor = new_prof
        each_class.save()
    print(f"Stored: {prof_name} for {each_class.courseID}")