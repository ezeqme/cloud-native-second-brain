---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Machine Learning + Data"
themes: ["AI ML", "Platform Engineering", "Storage Data"]
speakers: ["Ricardo Rocha", "Dejan Golubovic", "CERN"]
sched_url: https://kccnceu2021.sched.com/event/iE1w/building-and-managing-a-centralized-ml-platform-with-kubeflow-at-cern-ricardo-rocha-dejan-golubovic-cern
youtube_search_url: https://www.youtube.com/results?search_query=Building+and+Managing+a+Centralized+ML+Platform+with+Kubeflow+at+CERN+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Building and Managing a Centralized ML Platform with Kubeflow at CERN - Ricardo Rocha & Dejan Golubovic, CERN

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Machine Learning + Data]]
- Temas: [[AI ML]], [[Platform Engineering]], [[Storage Data]]
- País/cidade: Virtual / Virtual
- Speakers: Ricardo Rocha, Dejan Golubovic, CERN
- Schedule: https://kccnceu2021.sched.com/event/iE1w/building-and-managing-a-centralized-ml-platform-with-kubeflow-at-cern-ricardo-rocha-dejan-golubovic-cern
- Busca YouTube: https://www.youtube.com/results?search_query=Building+and+Managing+a+Centralized+ML+Platform+with+Kubeflow+at+CERN+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Building and Managing a Centralized ML Platform with Kubeflow at CERN.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE1w/building-and-managing-a-centralized-ml-platform-with-kubeflow-at-cern-ricardo-rocha-dejan-golubovic-cern
- YouTube search: https://www.youtube.com/results?search_query=Building+and+Managing+a+Centralized+ML+Platform+with+Kubeflow+at+CERN+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=HuWt1N8NFzU
- YouTube title: Building and Managing a Centralized ML Platform with Kubeflow at... Ricardo Rocha & Dejan Golubovic
- Match score: 0.914
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/building-and-managing-a-centralized-ml-platform-with-kubeflow-at-cern/HuWt1N8NFzU.txt
- Transcript chars: 23459
- Keywords: training, basically, clusters, cluster, learning, machine, distributed, gpu, notebooks, actually, submit, running, groups, pipelines, google, pipeline, inference, kubeflow

### Resumo baseado na transcript

hello everyone welcome to um our talk on building and managing a centralized machine learning platform with cook flow at cern uh we'll be talking about some work we've been doing the last few months and a service that we open to our users hello my name is dan gulovus i am a computing engineer in ceramcloud team my focus is on machine learning infrastructure services with kubernetes and i will present this talk with my colleague ricardo my name is ricardo i'm a computer engineer also in the cern

### Excerpt da transcript

hello everyone welcome to um our talk on building and managing a centralized machine learning platform with cook flow at cern uh we'll be talking about some work we've been doing the last few months and a service that we open to our users hello my name is dan gulovus i am a computing engineer in ceramcloud team my focus is on machine learning infrastructure services with kubernetes and i will present this talk with my colleague ricardo my name is ricardo i'm a computer engineer also in the cern cloud team i focus mostly on containers networking and more recently gpu's accelerators and also machine learning and i'm also a member of the technical oversight committee of the cncf as an end-user representative so today we'll we'll give a talk about uh service at cern but just a very quick overview of what cern is about so cern is the european laboratory for particle physics the largest particle physics laboratory in the world and we build like large scientific machines that allow us to do fundamental research the largest we have is the large hadron collider you probably heard of it it's a 27 kilometer perimeter particle accelerator that is 100 meters in the ground and where we accelerate two beams of protons to very close to the speed of light and we make them collide at very specific points where we build large experiments and you see here cms lhcp atlas and alice to have an idea of the size you can see the geneva airport here on the picture this is a an image of the accelerator itself in the tunnel and you can see all the magnets that help us beam the uh bend the beam so that it circulates in the in the accelerator and this is a picture of um of one of the detectors the cms detector compact moon solenoid it's uh in a cavern 40 meters by 40 meters also 100 meters underground and this is where we make the proton beams collide this detector and the others as well act like gigantic cameras where we take something like 40 million uh pictures a second and the result of this is a large amount of data that we need to store and analyze um we we collect and and store more than 70 petabytes of data every year and this is after a lot of filtering uh one of one detector like this can generate something like one petabyte of data per second uh so that's why we are constantly looking to new technologies that can help us handle this amount of data so the main motivation for our service is the expanded usage of machine learning in high energy physics different groups at cern w
