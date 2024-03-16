import * as React from 'react';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Card from '@mui/material/Card';
import Chip from '@mui/material/Chip';
import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid';
import Link from '@mui/material/Link';
import Stack from '@mui/material/Stack';
import Typography from '@mui/material/Typography';
import ChevronRightRoundedIcon from '@mui/icons-material/ChevronRightRounded';
import QueryStatsIcon from '@mui/icons-material/QueryStats';
import AutoStoriesIcon from '@mui/icons-material/AutoStories';
import PeopleIcon from '@mui/icons-material/People';
import serviceImage from '../assets/serve.jpg';
import storyImage from '../assets/story.jpg';
import studentImage from '../assets/students.jpg';


const items = [
  {
    icon: <AutoStoriesIcon />,
    title: 'Our Story',
    description:
      'Platinum emerged from a shared frustration among a group of students with the limitations of existing course search systems. Inspired to create a better solution, our journey began in January 2024. Since then, we have been dedicated to developing an intuitive platform that revolutionizes the way individuals discover and engage with educational content.',
    imageLight: `url(${storyImage})`
  },
  {
    icon: <PeopleIcon />,
    title: 'Who We Serve',
    description:
      'Platinum serves students, educators, and lifelong learners alike. Whether you are a high school student planning your academic path, a college student seeking courses aligned with your career goals, or a professional looking to expand your knowledge, Platinum is here to support your educational journey.',
    imageLight: `url(${studentImage})`
  },
  {
    icon: <QueryStatsIcon />,
    title: 'What We Offer',
    description:
      'Platinum offers a comprehensive platform for discovering, evaluating, and saving courses for your interests and goals. Our intelligent search capabilities, grade distribution insights, and integration with Rate My Professor & YouTube provide invaluable resources for making informed decisions about your educational path.',
    imageLight: `url(${serviceImage})`
  },
];

export default function Features() {
  const [selectedItemIndex, setSelectedItemIndex] = React.useState(0);

  const handleItemClick = (index) => {
    setSelectedItemIndex(index);
  };

  const selectedFeature = items[selectedItemIndex];

  return (
    <Container id="features" sx={{ py: { xs: 8, sm: 16 } }}>
      <Grid container spacing={6}>
        <Grid item xs={12} md={6}>
          <div>
            <Typography component="h2" variant="h4" sx={{ color: '#fff' }}>
              Turn your idea into reality
            </Typography>
            <Typography
              variant="body1"
              
              sx={{ mb: { xs: 2, sm: 4 }, color: '#fff'}}
            >
              Discover more about Platinum
            </Typography>
          </div>
          <Grid container item gap={1} sx={{ display: { xs: 'auto', sm: 'none' } }}>
            {items.map(({ title }, index) => (
              <Chip
                key={index}
                label={title}
                onClick={() => handleItemClick(index)}
                sx={{
                  borderColor: (theme) => {
                    if (theme.palette.mode === 'light') {
                      return selectedItemIndex === index ? 'primary.light' : '';
                    }
                    return selectedItemIndex === index ? 'primary.light' : '';
                  },
                  background: (theme) => {
                    if (theme.palette.mode === 'light') {
                      return selectedItemIndex === index ? 'none' : '';
                    }
                    return selectedItemIndex === index ? 'none' : '';
                  },
                  backgroundColor: selectedItemIndex === index ? 'primary.main' : '',
                  '& .MuiChip-label': {
                    color: selectedItemIndex === index ? '#fff' : '',
                  },
                }}
              />
            ))}
          </Grid>
          <Box
            component={Card}
            variant="outlined"
            sx={{
              display: { xs: 'auto', sm: 'none' },
              mt: 4,
            }}
          >
            <Box
              sx={{
                backgroundImage: `url(${selectedFeature.imageLight})`, // Use imageLight directly
                backgroundSize: '100% 100%', // This will stretch the image to fill the box completely
                backgroundPosition: 'center',
                minHeight: 280,
              }}
            />
            <Box sx={{ px: 2, pb: 2 }}>
              <Typography color="text.primary" variant="body2" fontWeight="bold">
                {selectedFeature.title}
              </Typography>
              <Typography color="text.secondary" variant="body2" sx={{ my: 0.5 }}>
                {selectedFeature.description}
              </Typography>
              <Link
                color="primary"
                variant="body2"
                fontWeight="bold"
                sx={{
                  display: 'inline-flex',
                  alignItems: 'center',
                  '& > svg': { transition: '0.2s' },
                  '&:hover > svg': { transform: 'translateX(2px)' },
                }}
              >
                <ChevronRightRoundedIcon
                  fontSize="small"
                  sx={{ mt: '1px', ml: '2px' }}
                />
              </Link>
            </Box>
          </Box>
          <Stack
            direction="column"
            justifyContent="center"
            alignItems="flex-start"
            spacing={2}
            useFlexGap
            sx={{ width: '100%', display: { xs: 'none', sm: 'flex' } }}
          >
            {items.map(({ icon, title, description }, index) => (
              <Card
                key={index}
                variant="outlined"
                component={Button}
                onClick={() => handleItemClick(index)}
                sx={{
                    p: 3,
                    height: 'fit-content',
                    width: '100%',
                    background: 'none',
                    backgroundColor: selectedItemIndex === index ? 'grey.200' : 'rgba(96, 125, 139, 0.5)', // Sets the background color to white when not selected, and grey when selected
                    borderColor: selectedItemIndex === index ? 'primary.main' : 'grey.300', // Sets border color to primary when selected, grey when not
                    '&:hover': {
                      backgroundColor: 'grey.100', // Changes background to a lighter grey when hovered
                      borderColor: 'primary.main', // Changes border color to primary when hovered
                    },
                  }}
                  
              >
                <Box
                  sx={{
                    width: '100%',
                    display: 'flex',
                    textAlign: 'left',
                    flexDirection: { xs: 'column', md: 'row' },
                    alignItems: { md: 'center' },
                    gap: 2.5,
                  }}
                >
                  <Box
                    sx={{
                      color: (theme) => {
                        if (theme.palette.mode === 'light') {
                          return selectedItemIndex === index
                            ? 'primary.main'
                            : 'grey.300';
                        }
                        return selectedItemIndex === index
                          ? 'primary.main'
                          : 'grey.700';
                      },
                    }}
                  >
                    {icon}
                  </Box>
                  <Box sx={{ textTransform: 'none' }}>
                    <Typography
                      color="text.primary"
                      variant="body2"
                      fontWeight="bold"
                    >
                      {title}
                    </Typography>
                    <Typography
                      color="text.secondary"
                      variant="body2"
                      sx={{ my: 0.5 }}
                    >
                      {description}
                    </Typography>
                  </Box>
                </Box>
              </Card>
            ))}
          </Stack>
        </Grid>
        <Grid
          item
          xs={12}
          md={6}
          sx={{ display: { xs: 'none', sm: 'flex' }, width: '100%' }}
        >
          <Card
            variant="outlined"
            sx={{
              height: '100%',
              width: '100%',
              display: { xs: 'none', sm: 'flex' },
              pointerEvents: 'none',
            }}
          >
            <Box
              sx={{
                m: 'auto',
                width: 600,
                height: 700,
                backgroundSize: 'cover',
                backgroundRepeat: 'no-repeat',
                backgroundImage: (theme) =>
                  theme.palette.mode === 'light'
                    ? items[selectedItemIndex].imageLight
                    : items[selectedItemIndex].imageDark,
              }}
            />
          </Card>
        </Grid>
      </Grid>
    </Container>
  );
}