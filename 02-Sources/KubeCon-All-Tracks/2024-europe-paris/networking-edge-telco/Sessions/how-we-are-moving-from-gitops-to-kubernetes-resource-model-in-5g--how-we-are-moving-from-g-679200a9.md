---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Networking + Edge + Telco"
themes: ["Networking", "GitOps Delivery", "Kubernetes Core"]
speakers: ["Joel Studler", "Ashan Senevirathne", "Swisscom"]
sched_url: https://kccnceu2024.sched.com/event/1YeN2/how-we-are-moving-from-gitops-to-kubernetes-resource-model-in-5g-core-joel-studler-ashan-senevirathne-swisscom
youtube_search_url: https://www.youtube.com/results?search_query=How+We+Are+Moving+from+GitOps+to+Kubernetes+Resource+Model+in+5G+Core+CNCF+KubeCon+2024
slides: []
status: parsed
---

# How We Are Moving from GitOps to Kubernetes Resource Model in 5G Core - Joel Studler & Ashan Senevirathne, Swisscom

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Networking + Edge + Telco]]
- Temas: [[Networking]], [[GitOps Delivery]], [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Joel Studler, Ashan Senevirathne, Swisscom
- Schedule: https://kccnceu2024.sched.com/event/1YeN2/how-we-are-moving-from-gitops-to-kubernetes-resource-model-in-5g-core-joel-studler-ashan-senevirathne-swisscom
- Busca YouTube: https://www.youtube.com/results?search_query=How+We+Are+Moving+from+GitOps+to+Kubernetes+Resource+Model+in+5G+Core+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre How We Are Moving from GitOps to Kubernetes Resource Model in 5G Core.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeN2/how-we-are-moving-from-gitops-to-kubernetes-resource-model-in-5g-core-joel-studler-ashan-senevirathne-swisscom
- YouTube search: https://www.youtube.com/results?search_query=How+We+Are+Moving+from+GitOps+to+Kubernetes+Resource+Model+in+5G+Core+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=crmTnB6Zwt8
- YouTube title: How We Are Moving from GitOps to Kubernetes Resource Model in 5G Core
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/how-we-are-moving-from-gitops-to-kubernetes-resource-model-in-5g-core/crmTnB6Zwt8.txt
- Transcript chars: 31212
- Keywords: configuration, config, basically, native, network, gitops, resource, static, automation, operator, reconciliation, dynamic, principles, netcon, management, flux, resources, practice

### Resumo baseado na transcript

so um hello everyone and welcome to to our session we are truly excited to present uh how we are moving from gitops to kubernetes a resource model in our 5G core so before we start the presentation um or we dive into the Telecommunications uh the world of telecommunications and its intersection with the gitops and the kubernetes worlds um I would like to get a feel of the audience first so could you please raise your hands if anyone's from the Telco domain or work in the Telco

### Excerpt da transcript

so um hello everyone and welcome to to our session we are truly excited to present uh how we are moving from gitops to kubernetes a resource model in our 5G core so before we start the presentation um or we dive into the Telecommunications uh the world of telecommunications and its intersection with the gitops and the kubernetes worlds um I would like to get a feel of the audience first so could you please raise your hands if anyone's from the Telco domain or work in the Telco area okay it's really nice to see we have a diverse audience today so let's uh start with an analogy imagine that you are going on a CrossCountry road trip um and you you want to go from uh point A to B and you have two options the first is a static uh paper map the other one is an application like Apple Maps or Google Maps so with the with the static map uh you can see that it's uh quite static uh the information or the the all what's in there it's quite fixed right and also it's unchanging and to the user end it's quite overwhelming on the other end uh you have Apple Maps it's quite Dynamic uh it also changes on the external conditions so if there are any um B due to the traffic conditions and such it will also uh recommend you different routes and such as it's more focused uh it also gives you simple way to navigate your path and these two examples it it really mirrors uh what we what we what we are going through in our journey in the 5G core so what we have now is a gp's way of uh implementation and our configuration it's quite static it's very similar to this static paper map and what we want to achieve in the end is a dynamic configuration uh with the introduction of gitops and uh kubernetes resource model so with that uh I would like to ruce myself my name is Ashan senat I am the product owner of the mobile Cloud native automation team and my name is yler I am a devops engineer in the same team you can find our contact info on the slides uh if you want to contact us so we both work for swisscom swisscom is one of the major or leading Telco and it providers in Switzerland not only that we're also moving from a Telco company to more like a tech company we call this the journey from Telco to Techo so when we talk about 5G core it's maybe important to distinguish what it means so 5G consists of two components the one component is the r the radio Access Network which basically makes sure that your cell phone can connect to the tower wirelessly and then you're you're being redirecte
