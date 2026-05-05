---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Project Opportunities"
themes: ["Project Opportunities"]
speakers: []
sched_url: https://kccnceu2024.sched.com/event/1aQhZ/how-crossplane-is-accelerating-your-cloud-native-control-plane-journey-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=How+Crossplane+is+Accelerating+Your+Cloud+Native+Control+Plane+Journey+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# How Crossplane is Accelerating Your Cloud Native Control Plane Journey | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Project Opportunities]]
- País/cidade: France / Paris
- Speakers: N/A
- Schedule: https://kccnceu2024.sched.com/event/1aQhZ/how-crossplane-is-accelerating-your-cloud-native-control-plane-journey-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=How+Crossplane+is+Accelerating+Your+Cloud+Native+Control+Plane+Journey+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre How Crossplane is Accelerating Your Cloud Native Control Plane Journey | Project Lightning Talk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1aQhZ/how-crossplane-is-accelerating-your-cloud-native-control-plane-journey-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=How+Crossplane+is+Accelerating+Your+Cloud+Native+Control+Plane+Journey+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=IslAWug5R7E
- YouTube title: How Crossplane is Accelerating Your Cloud Native Control Plane Journey | Project Lightning Talk
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/how-crossplane-is-accelerating-your-cloud-native-control-plane-journey/IslAWug5R7E.txt
- Transcript chars: 5132
- Keywords: resources, crossplane, everything, function, resource, cluster, command, waiting, functions, crossb, provider, information, thanks, native, behind, development, experience, improvements

### Resumo baseado na transcript

greetings everyone I'm esgi and this is Loro we are engineers at upbound who is the company behind crossplane and today we are going to talk about our recent crossplane development experience improvements specifically focusing on the crossplane CLI tooling I'm sure you all know about cross plane but let me start with in introducing it so crossplane is the cloud native solution for provisioning cloud resources it can uh encapsulate different resources or policies behind the single MPI so that users can self-service them uh and just start using

### Excerpt da transcript

greetings everyone I'm esgi and this is Loro we are engineers at upbound who is the company behind crossplane and today we are going to talk about our recent crossplane development experience improvements specifically focusing on the crossplane CLI tooling I'm sure you all know about cross plane but let me start with in introducing it so crossplane is the cloud native solution for provisioning cloud resources it can uh encapsulate different resources or policies behind the single MPI so that users can self-service them uh and just start using them without becoming an infrastructure expert it has lots of cool functionalities go check it out but due to our time constraint we cannot just cover all of them uh but we have a deep dive talk tomorrow so please join us and you can get more in depth knowledge with that talk okay so uh cross plan is awesome but uh as any project it has a lot of pain points so there are more than we have written here but uh I'll just go through this ones because for these ones we have some solutions uh some of those like where to start with writing providers or functions how to do it in a standard way uh writing compositions uh in crossb can be difficult uh the develop uh can be long and slow uh you can get everything ready and then you can have some validation error in in in your schemas because of some missing required fields for example or your crossb is running but your claim is not ready and you have to do a lot of digging to see what is going on so all of this can waste a lot of time and uh it's frustrating so uh lately in uh the cross team we have decided to invest into uh developer experience improvements uh some of those were uh focused on uh fixing and improving uh the developer the the development cycle and some are for uh making easier to work with close plane so uh to start uh oh by the way we uh we improved our clii so all of these commands are basically CLI commands that we have added to our CLI and I'll go through some of them uh so the first one is init so imagine that you have a cool idea about a new provider or a new function and you're thinking okay but what to do now go through dogs think about it uh how to start in a standard way well with uh in it you can now just uh use our CLI to initialize a repository for a function for a provider or a configuration we have a set of predefined uh template repositories uh but you can insert your own if uh if you would like and if the repository has a uh init script inside it
