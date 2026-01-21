# Overview
Its the turn of the New Year and I figured that it would be time to redo my portfolio website. Funny enough, it was around 11 months ago that I finished my [V2](https://kakumuo.github.io/portfolio/v2/index.html) set of changes. And some time before that I did my changes for [V1](https://kakumuo.github.io/portfolio/v1/index.html). I was never really happy with where I landed with either of these sites. The first was created as an ability to showcase my skills with JavaScript and HTML. I tried to force myself to understand what each of the most important elements were doing as well as being able to style them with CSS and JS. I event implemented some mouse-highjacking. In the next revision, I wanted to lean more towards React, but still trying to do things from *scratch*. With this revision, I looked to creating something that involved working with external APIs and differnt services. Styling was done in [TailwindCSS](https://tailwindcss.com/) and most of the components were from [MantineUI](https://mantine.dev/). I also limited my usage of any assistive technologies as to truly understand what I was doing. 

Originally, the idea of a portfolio came from losing my job and wanting to have something that recruiters can use to identify: 
- A real person
- That is looking to be hired
- And has the skills that they are looking for

If you are a recruiter, then {howdy!}[![](https://media1.tenor.com/m/GnMfIY8_sUoAAAAC/hello-woody.gif)]. But this ended up being more of an art project and something more explorative. The first two revisions were very much the former. However, at one point in time, I was trying to commit myself to writing on a daily basis as a new form of good habit. But that slowly started to fall off after a while. I figured that would pick it back up, but this time in the form of periodic entries in conjunction with my portfolio. 

## Features
I took heavy inspiration from one of the books that I'm reading ['The Pragmatic Programmer'](https://www.amazon.com/Pragmatic-Programmer-Journeyman-Master/dp/020161622X) by Andy Hunt, Dave Thomas. There the authors mentioned that they keep revisions of that book stored on Git. That would be the basis on how I would manage the blog posts. I'm sure that there's many tools to do the job, but I'd rather do it myself, at least once. Using Git gives me the added benefit of being able to pust revision details about the post and the project as changes are being made. 

Additionally, I took inspiration from another portfolio [site](https://www.8ty.one/) from Twitter user [@androidarts](https://x.com/androidarts). I've been following this person ever since their time as an artist on [Cortex Command](https://store.steampowered.com/app/209670/Cortex_Command/). I feel that they are the exact type of person that I would like to become when it comes to concept design (see [here](https://androidarts.com/)). They designed a monospaced [grid](https://8ty.one/status_grid/) that track and display project maturity. This also works well with the minimalistic format of their site, that of which I would also implement. The grid could be described as below: 
- The first three rows would represent the start and end dates of the project (YY, MM, DD).
- The last row would be for various statuses related to the project:
  - Type - *What kind of project is it*
    - **W**eb App
    - **D**esktop App
    - **G**ame Dev
    - **C**raft 
    - **M**usic
  - Size - *How large is the effort*
    - **S**mall 
    - **M**edium 
    - **L**arge 
    - e**X**tra Large
  - Complexity - *How involved is the effort*
    - **E**asy
    - **M**edium
    - **D**ifficult
  - Completion Status - *How far along is development*
    - **B**rainstorming
    - **I**nprogress
    - **C**omplete
    - **R**eleased
    - **D**ropped

The above sub-statuses are not set in stone. I don't know for sure if I want to keep the complexity status, but I feel that it also makes sense to identify the difference between complexity and size. You could have a project that is relatively small, but also very deep in what you can understand (anything math related). You can also have a project that is very large scale while also shallow in depth (ETL Development). 