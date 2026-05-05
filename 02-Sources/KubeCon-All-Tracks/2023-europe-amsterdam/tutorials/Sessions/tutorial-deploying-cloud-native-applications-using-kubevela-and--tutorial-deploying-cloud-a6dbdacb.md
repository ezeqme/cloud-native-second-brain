---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Tutorials"
themes: ["Tutorials"]
speakers: ["Daniel Higuero", "Napptive"]
sched_url: https://kccnceu2023.sched.com/event/1Hyaw/tutorial-deploying-cloud-native-applications-using-kubevela-and-oam-daniel-higuero-napptive
youtube_search_url: https://www.youtube.com/results?search_query=Tutorial%3A+Deploying+Cloud-Native+Applications+Using+Kubevela+and+OAM+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Tutorial: Deploying Cloud-Native Applications Using Kubevela and OAM - Daniel Higuero, Napptive

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Tutorials]]
- Temas: [[Tutorials]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Daniel Higuero, Napptive
- Schedule: https://kccnceu2023.sched.com/event/1Hyaw/tutorial-deploying-cloud-native-applications-using-kubevela-and-oam-daniel-higuero-napptive
- Busca YouTube: https://www.youtube.com/results?search_query=Tutorial%3A+Deploying+Cloud-Native+Applications+Using+Kubevela+and+OAM+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Tutorial: Deploying Cloud-Native Applications Using Kubevela and OAM.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1Hyaw/tutorial-deploying-cloud-native-applications-using-kubevela-and-oam-daniel-higuero-napptive
- YouTube search: https://www.youtube.com/results?search_query=Tutorial%3A+Deploying+Cloud-Native+Applications+Using+Kubevela+and+OAM+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_TGJF00IzWg
- YouTube title: Tutorial: Deploying Cloud-Native Applications Using Kubevela and OAM - Daniel Higuero, Napptive
- Match score: 0.928
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/tutorial-deploying-cloud-native-applications-using-kubevela-and-oam/_TGJF00IzWg.txt
- Transcript chars: 52921
- Keywords: application, basically, cluster, deploy, component, components, actually, create, applications, google, another, deployed, deployment, everything, workflow, continue, entities, operator

### Resumo baseado na transcript

um my name is Daniel liguero and I will be the one giving the tutorial to give you a little bit more information about me uh I'm the CTO at the company called native where we provide server as a service developer platform we use Google internally to as part as a building block for that platform and that is how I became interested in the project how we started learning about OEM and Cuba Bella and I am one of the Google maintainers my background basically is on Big

### Excerpt da transcript

um my name is Daniel liguero and I will be the one giving the tutorial to give you a little bit more information about me uh I'm the CTO at the company called native where we provide server as a service developer platform we use Google internally to as part as a building block for that platform and that is how I became interested in the project how we started learning about OEM and Cuba Bella and I am one of the Google maintainers my background basically is on Big Data Technologies at the very beginning of my career then I move into a streaming machine learning model building platforms that enable you to basically run that then I move into Edge Computing and after that I move into more of the developer platform area right this is going to be as I said before an intro to Google if you have further questions or more detail a specific questions outside of the topic of this tutorial feel free to come by by the booth there is a cncf booth I will be there later after the talk tomorrow also so feel free to come by and just ask any question right so the agenda for today will be first of all we will talk a little bit about what is the open application model uh what is Cuba Bella identifying two different elements then we will move into creating a small cluster with kind to install Cuba Bella and start deploying our own applications we will go through basic operations with the Bella CLI Bella ux we will go a little bit about the workflows that are automatically available in the applications we will give you a brief description of how you can enable multi-cluster deployments and how you can integrate with an aggigo environment and finally it's an extra context after that any question that combined I'm really happy to to answer both of them right so for this tutorial this is the link with the associated content we will go through the elements of this repository this is where the step-by-step instructions of how to get the Clusters are located so basically for this tutorial we'll be switching in between the code editor the terminals and things like that right so just uh where we need and we will continue through that okay so let's start first by explaining a little bit what is the open application model because it's something that is quietly related with Google but sometimes it gets easily confused right so the open application model is basically the specification on how you are going to express your own applications the idea here is to provide a high level abstraction
