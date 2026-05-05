---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Customizing + Extending Kubernetes"
themes: ["Kubernetes Core"]
speakers: ["Adam Wolfe Gordon", "DigitalOcean"]
sched_url: https://kccnceu2023.sched.com/event/1HyVZ/what-happened-to-the-service-catalog-adam-wolfe-gordon-digitalocean
youtube_search_url: https://www.youtube.com/results?search_query=What+Happened+to+the+Service+Catalog%3F+CNCF+KubeCon+2023
slides: []
status: parsed
---

# What Happened to the Service Catalog? - Adam Wolfe Gordon, DigitalOcean

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Customizing + Extending Kubernetes]]
- Temas: [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Adam Wolfe Gordon, DigitalOcean
- Schedule: https://kccnceu2023.sched.com/event/1HyVZ/what-happened-to-the-service-catalog-adam-wolfe-gordon-digitalocean
- Busca YouTube: https://www.youtube.com/results?search_query=What+Happened+to+the+Service+Catalog%3F+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre What Happened to the Service Catalog?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyVZ/what-happened-to-the-service-catalog-adam-wolfe-gordon-digitalocean
- YouTube search: https://www.youtube.com/results?search_query=What+Happened+to+the+Service+Catalog%3F+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=3LxqF1LdTDQ
- YouTube title: What Happened to the Service Catalog? - Adam Wolfe Gordon, DigitalOcean
- Match score: 0.779
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/what-happened-to-the-service-catalog/3LxqF1LdTDQ.txt
- Transcript chars: 31558
- Keywords: catalog, provider, operator, providers, operators, manage, application, instance, actually, talked, cluster, cross-plane, little, create, implement, infrastructure, binding, resources

### Resumo baseado na transcript

thanks for being here everyone I'm I'm Adam I work at digitalocean um I'm going to talk today about what happened to the service catalog and before I start I want to say I'm very happy to be here I was supposed to be here in Amsterdam in 2020 to give a talk and then the global pandemic started and I had to give that talk a loan in my office online which was not as fun as as being here with everybody uh so thanks for for coming today

### Excerpt da transcript

thanks for being here everyone I'm I'm Adam I work at digitalocean um I'm going to talk today about what happened to the service catalog and before I start I want to say I'm very happy to be here I was supposed to be here in Amsterdam in 2020 to give a talk and then the global pandemic started and I had to give that talk a loan in my office online which was not as fun as as being here with everybody uh so thanks for for coming today and really enjoying uh being here at kubecon so today I'm going to talk about the service catalog and service catalog was a kubernetes Sig and a kubernetes project started around 2016 and it shut down last year in 2022 and at least nominally this talk is about why it shut down what happened to it um but really what I want to talk about is something a little bit broader which is how we consume external services from applications running under kubernetes and the way that we manage those services so service catalog was uh one attempt at doing this this is what it was for but I think it's sort of more constructive maybe to talk about the solutions that have replaced it what people are using today and maybe some directions for the future um and things that we can do going forward to solve this problem a little bit better so um I don't usually put this kind of slide in my talks because I don't think you actually care that much about me personally um your care more about the topic but today I am going to give some opinions and so I think it's important that you know sort of where I'm coming from what my biases are so I'm going to talk a little bit about myself um again I'm Adam wolf Gordon I work at digitalocean UH digitalocean is a cloud provider we provide all the things that a cloud provider might provide like virtual machines and managed kubernetes manage databases Network things um and these days I work on our product strategy group so I work across all our products helping align roadmaps and think about what our customers need and that sort of thing but before this I I was the tech lead for our managed kubernetes and container registry products for the last few years and one of the things I thought about a lot in that role is the way that our customers put all the pieces together that we offer to support their applications no application is an island they do need other things and our customers need to put those pieces together to be effective um so that's kind of the background of this talk is thinking about that problem and bef
