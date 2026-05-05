---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Machine Learning + Data"
themes: ["AI ML", "Storage Data", "SRE Reliability"]
speakers: ["Keshi Dai", "Jonathan Jin", "Spotify"]
sched_url: https://kccncna2021.sched.com/event/lV4l/scaling-kubeflow-for-multi-tenancy-at-spotify-keshi-dai-jonathan-jin-spotify
youtube_search_url: https://www.youtube.com/results?search_query=Scaling+Kubeflow+for+Multi-tenancy+at+Spotify+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Scaling Kubeflow for Multi-tenancy at Spotify - Keshi Dai & Jonathan Jin, Spotify

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Machine Learning + Data]]
- Temas: [[AI ML]], [[Storage Data]], [[SRE Reliability]]
- País/cidade: United States / Los Angeles
- Speakers: Keshi Dai, Jonathan Jin, Spotify
- Schedule: https://kccncna2021.sched.com/event/lV4l/scaling-kubeflow-for-multi-tenancy-at-spotify-keshi-dai-jonathan-jin-spotify
- Busca YouTube: https://www.youtube.com/results?search_query=Scaling+Kubeflow+for+Multi-tenancy+at+Spotify+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Scaling Kubeflow for Multi-tenancy at Spotify.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV4l/scaling-kubeflow-for-multi-tenancy-at-spotify-keshi-dai-jonathan-jin-spotify
- YouTube search: https://www.youtube.com/results?search_query=Scaling+Kubeflow+for+Multi-tenancy+at+Spotify+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=KUyEuY5ZSqI
- YouTube title: Scaling Kubeflow for Multi-tenancy at Spotify - Keshi Dai & Jonathan Jin, Spotify
- Match score: 0.824
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/scaling-kubeflow-for-multi-tenancy-at-spotify/KUyEuY5ZSqI.txt
- Transcript chars: 27820
- Keywords: cluster, platform, clusters, kubeflow, pipeline, namespace, metrics, resources, spotify, infrastructure, changes, terraform, pipelines, manage, resource, support, deployment, profile

### Resumo baseado na transcript

hello everyone and welcome to the cubicle talk on scaling keep flow for multi tenancy at spotify today jonathan and i are going to share the story on how we scale up our cube flow platform to serve the growing number of ml teams at spotify let's start with the introduction my name is cash dai i'm a senior ml info engineer at spotify this is my teammate jonathan jean also a senior engineer you will hear from him during the later part of this talk so we are spotify

### Excerpt da transcript

hello everyone and welcome to the cubicle talk on scaling keep flow for multi tenancy at spotify today jonathan and i are going to share the story on how we scale up our cube flow platform to serve the growing number of ml teams at spotify let's start with the introduction my name is cash dai i'm a senior ml info engineer at spotify this is my teammate jonathan jean also a senior engineer you will hear from him during the later part of this talk so we are spotify if you haven't heard of us before we an audio streaming service we launched in 2008 and now we have more than 365 million monthly active users on our platform we have more than 70 million tracks and almost 3 million podcast titles and our service is available in 178 markets all over the world machine learning is at the heart of almost everything we do at spotify including recommending personalized content on home page optimizing the ranking results from the search or helping you discover and explore the music you haven't listened to before it enables us to recommend artists playlists and podcasts to keep our users active engaged and more likely to subscribe in the long term to power ml products at spotify our team is building a standardized machine learning platform to provide our engineers with tools and environment to quickly prototype experiment and productionize their ml ideas our platform internally known as qfloor platform consists of two major components a python sdk for building ml workflow with tfx components and several managed kubeflow gke clusters for mr pipeline executions for those who don't know tfx tensorflow extended is a component-based ml framework around tens flow ecosystems qflow is a set of machine learning toolkits on top of kubernetes on our platform we mainly use kubeflow pipelines to orchestrate ml workflows built with tfx this is a typical ml workflow and spotify as you can see it has a sequence of components representing different steps in a machine learning pipeline it starts with future engineering future collector and transform components assemble the raw features and transform them into the meaningful ones for model training next we have stats and schema generation components to validate those features and produce a schema file based on the future data stats then we have the trainer component for model training and evaluate component for the model performance analysis in the end hopefully everything looks good then we can deploy the model to production through the d
