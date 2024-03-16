import * as React from 'react';
import Card from '@mui/material/Card';
import CardHeader from '@mui/material/CardHeader';
import CardContent from '@mui/material/CardContent';
import Avatar from '@mui/material/Avatar';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid';
import { useTheme } from '@mui/system';
import kevinImage from '../assets/kevin.png';
import ivanImage from '../assets/Ivan.jpg';
import marianaImage from '../assets/Mariana.jpg';
import leoImage from '../assets/Leo.jpg';
import yicongImage from '../assets/yicong.png';
import shuyiImage from '../assets/Sherry.jpg';
import claireImage from '../assets/claire.jpg';
import katzImage from '../assets/katz.jpg';



const userTestimonials = [
  {
    avatar: <Avatar alt="Kevin Nguyen" src={kevinImage} />,
    name: 'Kevin Nguyen',
    /* occupation: 'Backend Engineer', */
    testimonial:
      "Python and C++ enthusiast",
  },
  {
    avatar: <Avatar alt="Shuyi Wan" src={shuyiImage} />,
    name: 'Shuyi Wan',
    /* occupation: 'Backend Engineer', */
    testimonial:
      "Muda muda muda!",
  },
  {
    avatar: <Avatar alt="Yicong Yan" src={yicongImage} />,
    name: 'Yicong Yan',
    /* occupation: 'Backend Engineer', */
    testimonial:
      'Street Fighter 6 Player',
  },
  {
    avatar: <Avatar alt="Leo Guo" src={leoImage} />,
    name: 'Leo Guo',
    /* occupation: 'Backend Engineer', */
    testimonial:
      `def joke():
      if (1 == 0):
          return "Why did the programmer go broke?"
      else:
          return "Because he used up all his cache!"
  `},
  {
    avatar: <Avatar alt="Katz Yan" src={katzImage} />,
    name: 'Katz Yan',
    /* occupation: 'Backend Engineer', */
    testimonial:
      "A student who always starts working at the last minute.",
  },
  {
    avatar: <Avatar alt="Claire Pemberton" src={claireImage} />,
    name: 'Claire Pemberton',
    /* occupation: 'Backend Engineer', */
    testimonial:
      'Error 4:04 sleep not found',
  },
  {
    avatar: <Avatar alt="Mariana Rosillo" src={marianaImage} />,
    name: 'Mariana Rosillo',
    /* occupation: 'Backend Engineer', */
    testimonial:
      'If you ever get stuck, just git rebase —abort',
  },
  {
    avatar: <Avatar alt="Ivan Hernandez" src={ivanImage} />,
    name: 'Ivan Hernandez',
    /* occupation: 'Backend Engineer', */
    testimonial:
      'When in doubt, use git push—force, and that’ll do it. ',
  },
];

export default function Testimonials() {
  const theme = useTheme();

  return (
    <Container
      id="testimonials"
      sx={{
        pt: { xs: 4, sm: 12 },
        pb: { xs: 8, sm: 16 },
        position: 'relative',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        gap: { xs: 3, sm: 6 },
      }}
    >
      <Box
        sx={{
          width: { sm: '100%', md: '60%' },
          textAlign: { sm: 'left', md: 'center' },
        }}
      >
        <Typography component="h2" variant="h4" color="text.primary" sx = {{color:'white'}}>
          Our Team
        </Typography>
        <Typography variant="body1" color="text.secondary"sx = {{color:'white'}}>
          See what our customers love about our products. Discover how we excel in
          efficiency, durability, and satisfaction. Join us for quality, innovation,
          and reliable support.
        </Typography>
      </Box>
      <Grid container spacing={2}>
        {userTestimonials.map((testimonial, index) => (
          <Grid item xs={12} sm={6} md={4} key={index} sx={{ display: 'flex' }}>
            <Card
              sx={{
                display: 'flex',
                flexDirection: 'column',
                justifyContent: 'space-between',
                flexGrow: 1,
                p: 1,
              }}
            >
              <CardContent>
                <Typography variant="body2" color="text.secondary">
                  {testimonial.testimonial}
                </Typography>
              </CardContent>
              <Box
                sx={{
                  display: 'flex',
                  flexDirection: 'row',
                  justifyContent: 'space-between',
                  pr: 2,
                }}
              >
                <CardHeader
                  avatar={testimonial.avatar}
                  title={testimonial.name}
                  subheader={testimonial.occupation}
                />
              </Box>
            </Card>
          </Grid>
        ))}
      </Grid>
    </Container>
  );
}
