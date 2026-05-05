---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "SDLC"
themes: ["GitOps Delivery"]
speakers: ["Alexander Zielenski", "Google", "Stefan Schimanski", "Upbound"]
sched_url: https://kccnceu2024.sched.com/event/1YeNx/shift-left-past-present-and-future-of-validation-in-ci-for-gitops-workflows-alexander-zielenski-google-stefan-schimanski-upbound
youtube_search_url: https://www.youtube.com/results?search_query=Shift-Left%3A+Past%2C+Present%2C+and+Future+of+Validation+in+CI+for+GitOps+Workflows+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Shift-Left: Past, Present, and Future of Validation in CI for GitOps Workflows - Alexander Zielenski, Google & Stefan Schimanski, Upbound

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[SDLC]]
- Temas: [[GitOps Delivery]]
- País/cidade: France / Paris
- Speakers: Alexander Zielenski, Google, Stefan Schimanski, Upbound
- Schedule: https://kccnceu2024.sched.com/event/1YeNx/shift-left-past-present-and-future-of-validation-in-ci-for-gitops-workflows-alexander-zielenski-google-stefan-schimanski-upbound
- Busca YouTube: https://www.youtube.com/results?search_query=Shift-Left%3A+Past%2C+Present%2C+and+Future+of+Validation+in+CI+for+GitOps+Workflows+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Shift-Left: Past, Present, and Future of Validation in CI for GitOps Workflows.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeNx/shift-left-past-present-and-future-of-validation-in-ci-for-gitops-workflows-alexander-zielenski-google-stefan-schimanski-upbound
- YouTube search: https://www.youtube.com/results?search_query=Shift-Left%3A+Past%2C+Present%2C+and+Future+of+Validation+in+CI+for+GitOps+Workflows+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=KaXIq8Qv77A
- YouTube title: Shift-Left: Past, Present, and Future of Validation in CI... Alexander Zielenski & Stefan Schimanski
- Match score: 0.811
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/shift-left-past-present-and-future-of-validation-in-ci-for-gitops-work/KaXIq8Qv77A.txt
- Transcript chars: 23479
- Keywords: validation, schemas, replicas, validations, basically, schema, object, cluster, validate, server, native, specify, everybody, everything, client, access, create, resource

### Resumo baseado na transcript

but today we want to talk about validation so validation is something I think everybody used in the last 10 years especially when you build things on kubernetes and using cads and this is basically the topic but not only cads but also native types at the end validation so shift left what is shift left cryptic term we will see it in a second and we we will talk about the past so we will have basically a little history session what we added over the 10 years what

### Excerpt da transcript

but today we want to talk about validation so validation is something I think everybody used in the last 10 years especially when you build things on kubernetes and using cads and this is basically the topic but not only cads but also native types at the end validation so shift left what is shift left cryptic term we will see it in a second and we we will talk about the past so we will have basically a little history session what we added over the 10 years what we're doing at the moment and where we want to go to and why we do all of that like validation has been in kuber since day one basically but we are not finished and we will see why and what the next big topics are so let's start in 2015 so this is like yeah very much in the beginning of kubernetes and shortly later CS came up but it was not there in so everybody knows that when KU was built especially the cube cutle tool Cube cutle create everybody knows that when this was built this was a model like you have a manifest file some deployment jaml and you say Cube CLE create and there was a mistake right you saw you see now I type secret name secret names cannot be right and the server basically not noticed that and tells you okay there's a mistake fix it super fast super nice and kind of a new user experience which was not so common at the time but this is 2015 and 2024 looks very very different so the reality is this probably most people um have the ICD in place so we have this long pipeline you have your developer notebook you type you white gaml manifests and you commit to get to some Branch you proof it pull request and everything your GitHub action start running and they check some something hopefully they they find this mistake but if they don't find it cosplan or Aro CD or some other gups tool will deploy your code into production and the CU will notice maybe will not notice if you mistype the field because it's a typo right a typo is for for the API server it's not a mistake right it can be just U that you have a new version of the Manifest and the server is old so intentionally it it might accept it even even worse so you change has no effect but basically we have no Cube cutle more anymore as a primary tool to apply manifests so shifting left is basically shifting this lightning there at the top that's where you notice the mistake shifted left very visually shifted left feedback after 10 minutes plus is not acceptable it's not an inner loop that's like take two coffees and then you can see
