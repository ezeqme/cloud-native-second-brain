---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Unclassified"
themes: ["AI ML", "Storage Data", "GitOps Delivery", "SRE Reliability"]
speakers: ["Luca Grazioli", "Dennis Ohrndorf", "DHL Data", "Analytics"]
sched_url: https://kccnceu2024.sched.com/event/1YePL/from-bash-scripts-to-kubeflow-and-gitops-our-journey-to-operationalizing-ml-at-scale-luca-grazioli-dennis-ohrndorf-dhl-data-analytics
youtube_search_url: https://www.youtube.com/results?search_query=From+Bash+Scripts+to+Kubeflow+and+GitOps%3A+Our+Journey+to+Operationalizing+ML+at+Scale+CNCF+KubeCon+2024
slides: []
status: parsed
---

# From Bash Scripts to Kubeflow and GitOps: Our Journey to Operationalizing ML at Scale - Luca Grazioli & Dennis Ohrndorf, DHL Data & Analytics

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Unclassified]]
- Temas: [[AI ML]], [[Storage Data]], [[GitOps Delivery]], [[SRE Reliability]]
- País/cidade: France / Paris
- Speakers: Luca Grazioli, Dennis Ohrndorf, DHL Data, Analytics
- Schedule: https://kccnceu2024.sched.com/event/1YePL/from-bash-scripts-to-kubeflow-and-gitops-our-journey-to-operationalizing-ml-at-scale-luca-grazioli-dennis-ohrndorf-dhl-data-analytics
- Busca YouTube: https://www.youtube.com/results?search_query=From+Bash+Scripts+to+Kubeflow+and+GitOps%3A+Our+Journey+to+Operationalizing+ML+at+Scale+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre From Bash Scripts to Kubeflow and GitOps: Our Journey to Operationalizing ML at Scale.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YePL/from-bash-scripts-to-kubeflow-and-gitops-our-journey-to-operationalizing-ml-at-scale-luca-grazioli-dennis-ohrndorf-dhl-data-analytics
- YouTube search: https://www.youtube.com/results?search_query=From+Bash+Scripts+to+Kubeflow+and+GitOps%3A+Our+Journey+to+Operationalizing+ML+at+Scale+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=dwt-MBEUGpQ
- YouTube title: From Bash Scripts to Kubeflow and GitOps: Our Journey to Operationalizing ML at Scale
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/from-bash-scripts-to-kubeflow-and-gitops-our-journey-to-operationalizi/dwt-MBEUGpQ.txt
- Transcript chars: 31600
- Keywords: machine, learning, platform, important, actually, projects, engineers, started, production, usually, notebooks, pipelines, course, science, business, process, certain, everything

### Resumo baseado na transcript

nice to see you guys you so many are you sure that you're in the right talk I'm not so sure about that uh so welcome to our session uh today we're going to walk you through our journey in DHL in how we adopted Cube flow as our main platform for operationalizing machine learning at scale meaning what we've all the steps that we have to go through starting from B scripts till our current solution and our our setup I'm luuka alongside with me it's Dennis we are

### Excerpt da transcript

nice to see you guys you so many are you sure that you're in the right talk I'm not so sure about that uh so welcome to our session uh today we're going to walk you through our journey in DHL in how we adopted Cube flow as our main platform for operationalizing machine learning at scale meaning what we've all the steps that we have to go through starting from B scripts till our current solution and our our setup I'm luuka alongside with me it's Dennis we are both part of the mlops engineering team I'm lead mlop engineer I joined thehl less than one year ago but I'm a longtime mlops engineer I started in 2018 but I also have a background as a data scientist and I've used Cube flow in different setups this is the largest setups that I use Cube flow but I'm also here not to just to represent DHL but also to represent Cube flow from a user perspective I used it from very small companies to bigger one and we will go also through some of the journey that even outside of DHL we we can I've gone through in the past so alongside with me there is Dennis thank you Luca um yeah also very well welcome from my side uh I'm Dennis it's really crazy to see such a huge crowd um uh my name is Dennis I'm senior mlops engineer in the DHL data and analytics um Team um I started as a data scientist actually in 2020 so uh roughly four years in the company now building machine learning applications for DHL group I moved or transition to the whole domain of mlops engineering so machine learning operations roughly in 2021 when we um started also to to scale our Solutions um and and yeah productionize them uh four years of cube flow um that's pretty important I think because today we are also going to give you a little bit of a rundown of our um experience that we have from um starting with a practical setup to now having like a very sophisticated setup where we can also um yeah leverage uh Cube flow ASR data science platform and I have been part of this journey for the last four years as well um I want to briefly give you a very short overview of our company so we are called DHL data and analytics uh we are part of DHL group uh I guess all of you know who DH group is so they will probably at some point have delivered some package to you or maybe even Formula 1 cars we don't know uh so we are a huge Logistics partner also for Formula 1 um but specifically our team of DHL data and analytics um we are doing machine learning projects for the whole group for roughly uh 7 to eight years n
