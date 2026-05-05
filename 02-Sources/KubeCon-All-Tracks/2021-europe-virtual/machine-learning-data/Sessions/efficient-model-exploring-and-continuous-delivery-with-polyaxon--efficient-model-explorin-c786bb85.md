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
themes: ["AI ML", "Storage Data", "GitOps Delivery"]
speakers: ["Shotaro Kohama", "Mercari Inc"]
sched_url: https://kccnceu2021.sched.com/event/iE5c/efficient-model-exploring-and-continuous-delivery-with-polyaxon-+-kubeflow-shotaro-kohama-mercari-inc
youtube_search_url: https://www.youtube.com/results?search_query=Efficient+Model+Exploring+and+Continuous+Delivery+With+Polyaxon+%2B+Kubeflow+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Efficient Model Exploring and Continuous Delivery With Polyaxon + Kubeflow - Shotaro Kohama, Mercari Inc

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Machine Learning + Data]]
- Temas: [[AI ML]], [[Storage Data]], [[GitOps Delivery]]
- País/cidade: Virtual / Virtual
- Speakers: Shotaro Kohama, Mercari Inc
- Schedule: https://kccnceu2021.sched.com/event/iE5c/efficient-model-exploring-and-continuous-delivery-with-polyaxon-+-kubeflow-shotaro-kohama-mercari-inc
- Busca YouTube: https://www.youtube.com/results?search_query=Efficient+Model+Exploring+and+Continuous+Delivery+With+Polyaxon+%2B+Kubeflow+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Efficient Model Exploring and Continuous Delivery With Polyaxon + Kubeflow.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE5c/efficient-model-exploring-and-continuous-delivery-with-polyaxon-+-kubeflow-shotaro-kohama-mercari-inc
- YouTube search: https://www.youtube.com/results?search_query=Efficient+Model+Exploring+and+Continuous+Delivery+With+Polyaxon+%2B+Kubeflow+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=YMIVVexph4c
- YouTube title: Efficient Model Exploring and Continuous Delivery With Polyaxon + Kubeflow - Shotaro Kohama
- Match score: 0.986
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/efficient-model-exploring-and-continuous-delivery-with-polyaxon-kubefl/YMIVVexph4c.txt
- Transcript chars: 12283
- Keywords: pipeline, continuous, training, component, learning, machine, production, cubicle, python, development, docker, feature, define, create, integration, workflow, submit, polyaccent

### Resumo baseado na transcript

hi welcome to my call i'm shotalo i'm a machine learning platform engineer at bell party today i'm going to talk about efficient modern exploring and continuous daily value polyaccent and the cubic row let's get started first of all i will explain what melton is mentally is a customer to customer marketplace where customers can sell their items to the other customers the balcony is available in the us and japan today i'm going to talk about the meltdown u.s massive learning platforms award one of our unique challenges

### Excerpt da transcript

hi welcome to my call i'm shotalo i'm a machine learning platform engineer at bell party today i'm going to talk about efficient modern exploring and continuous daily value polyaccent and the cubic row let's get started first of all i will explain what melton is mentally is a customer to customer marketplace where customers can sell their items to the other customers the balcony is available in the us and japan today i'm going to talk about the meltdown u.s massive learning platforms award one of our unique challenges is pricing for sellers if the item price is too expensive that it takes time to draw studio on the other hand if the item is too affordable the seller cannot make a profitable sales to help to solve this problem we use these machine learning models we call that system applies guidance system that class guidance system consists of the two features one is the applied suggestion apply suggestion feature recommends a viable price range when the customer makes a listing on our marketplace and the second feature is smart pricing when the customer make a listing on our marketplace customer account besides the blue applies and smart plus in the future gradually and automatically update that item flies to the floor flies and then that the item will be promoted to the potential buyers to design item price lunch and floor plans we use this machine learning model our machine learning model takes the item title description in category and so on and the suggested prices we use machine learning practical components behind this price guidance system so in the latter part of this presentation i will dive into that machine learning component here is the today's agenda first i will talk about the general machine learning project life cycle and then i will explain that how we use the polyaxon and the cube flow pipeline of melatonin lastly i will talk about how we build the machine learning platform to utilize that uh polyaccinto pipeline efficiency let's move on to the first part what's in learning development time life cycle generally speaking machine learning projects are highly iterative first we need to design the task to solve the sml and once we design that task then we'll start the collecting training data and we got the enough training data we can start the model exploring phase through the model exploring phase we decide that our first model to deploy to the production and then we can start the development microservice to deploy our model and integrate
