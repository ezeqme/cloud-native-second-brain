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
speakers: ["David Hadas", "Michael Maximilien", "IBM"]
sched_url: https://kccnceu2023.sched.com/event/1HyWL/use-knative-when-you-can-and-kubernetes-when-you-must-david-hadas-michael-maximilien-ibm
youtube_search_url: https://www.youtube.com/results?search_query=Use+Knative+When+You+Can%2C+and+Kubernetes+When+You+Must+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Use Knative When You Can, and Kubernetes When You Must - David Hadas & Michael Maximilien, IBM

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Customizing + Extending Kubernetes]]
- Temas: [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: David Hadas, Michael Maximilien, IBM
- Schedule: https://kccnceu2023.sched.com/event/1HyWL/use-knative-when-you-can-and-kubernetes-when-you-must-david-hadas-michael-maximilien-ibm
- Busca YouTube: https://www.youtube.com/results?search_query=Use+Knative+When+You+Can%2C+and+Kubernetes+When+You+Must+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Use Knative When You Can, and Kubernetes When You Must.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyWL/use-knative-when-you-can-and-kubernetes-when-you-must-david-hadas-michael-maximilien-ibm
- YouTube search: https://www.youtube.com/results?search_query=Use+Knative+When+You+Can%2C+and+Kubernetes+When+You+Must+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=0IwysONytqc
- YouTube title: Use Knative When You Can, and Kubernetes When You Must - David Hadas & Michael Maximilien, IBM
- Match score: 0.832
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/use-knative-when-you-can-and-kubernetes-when-you-must/0IwysONytqc.txt
- Transcript chars: 29197
- Keywords: native, k-native, deploy, everything, revision, security, microservices, number, serverless, actually, running, resources, change, course, instance, configuration, energy, scaling

### Resumo baseado na transcript

so I am Max um and I work I'm a distinguished engineer at IBM and actually I was one of the people after Google made k-native public to uh start contributing to it obviously lots of folks from Red Hat VMware you know I'm sure I'm gonna forget some names but the project has grown especially the folks that created chain guard most of them were from Google and then they created a native um and I worked on that for about two years or two and a half years new Services then those functions at the end of the day are just container images and those container images are running serverless so it's a native kubernetes service so so now we make a distinction between running against kubernetes and in that case we talked you are able to eliminate them through some magical way which is an auto scaler then you only have a bunch of PODS that you can control and you know that are actively working this will give you in the future as we move forward up a VM let's be honest um so that's another benefit that we have um which comes with the with K native the second thing is okay we we are using microservices most of us are developing micro services for kubernetes microservices were designed in

### Excerpt da transcript

so I am Max um and I work I'm a distinguished engineer at IBM and actually I was one of the people after Google made k-native public to uh start contributing to it obviously lots of folks from Red Hat VMware you know I'm sure I'm gonna forget some names but the project has grown especially the folks that created chain guard most of them were from Google and then they created a native um and I worked on that for about two years or two and a half years and then now I'm working actually on sort of what we call Quantum serverless so it actually uses K native underneath but my mission is bordered and just that it's actually um you know Quantum open quantum so we're not going to talk about that now that was the talk before that's why I was late but I'm here with my colleague David Harris and actually I'll give a lot of credit to David for this talk not only for putting it together but also it came from a blog post that he had so David Works uh and startup Nation anybody knows where that is you all know Silicon Valley right but there is a country called startup Nation yes I've never been but I've collaborated with so many people from Israel that it's probably true it's startup Nation so anyway he's from there he worked 10 years I think trying to build startups and then you give up and join us and he's an expert in security and when he contacted me to help in k-native he's made a big difference so he's going to talk about some of the work that he's also doing but what's interesting about this talk is that it tries to position K native as the place you should start so let's get to it so obviously you know when you're talking about cloud computing um you know in terms of the big picture right it's pretty much what everybody is using so I'm you know here because you know with this is cloud native and people are using cloud computing for all types of you know problems solving problems even Quantum which is what you know I just came back from a talk on that but there is some downside to it and we wrote a blog post at least for some aspects of this so starting from the bottom for instance I think yesterday if you are the keynote uh folks colleagues from Azure are talking about this as well as red hat where there is actually a lot of energy that's being consumed by those data centers and if we keep going in that direction uh it's not going to help the problem that we all face I mean I don't have to tell you we all you know hopefully you're not a climate denier but if you
