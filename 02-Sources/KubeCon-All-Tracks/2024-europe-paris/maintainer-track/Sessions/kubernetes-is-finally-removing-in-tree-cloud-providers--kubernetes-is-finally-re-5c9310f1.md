---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Maintainer Track"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Bridget Kromhout", "Microsoft", "Chris Privitere", "Equinix"]
sched_url: https://kccnceu2024.sched.com/event/1Yhhh/kubernetes-is-finally-removing-in-tree-cloud-providers-bridget-kromhout-microsoft-chris-privitere-equinix
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+Is+FINALLY+Removing+in-Tree+Cloud+Providers+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Kubernetes Is FINALLY Removing in-Tree Cloud Providers - Bridget Kromhout, Microsoft & Chris Privitere, Equinix

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: Bridget Kromhout, Microsoft, Chris Privitere, Equinix
- Schedule: https://kccnceu2024.sched.com/event/1Yhhh/kubernetes-is-finally-removing-in-tree-cloud-providers-bridget-kromhout-microsoft-chris-privitere-equinix
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+Is+FINALLY+Removing+in-Tree+Cloud+Providers+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Kubernetes Is FINALLY Removing in-Tree Cloud Providers.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1Yhhh/kubernetes-is-finally-removing-in-tree-cloud-providers-bridget-kromhout-microsoft-chris-privitere-equinix
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+Is+FINALLY+Removing+in-Tree+Cloud+Providers+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=IIxQHQHOXs4
- YouTube title: Kubernetes Is FINALLY Removing in-Tree Cloud Providers - Bridget Kromhout & Chris Privitere
- Match score: 0.846
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/kubernetes-is-finally-removing-in-tree-cloud-providers/IIxQHQHOXs4.txt
- Transcript chars: 28971
- Keywords: provider, providers, controller, little, manager, equinex, release, finally, thinking, specific, cluster, absolutely, change, github, infrastructure, starting, looking, talked

### Resumo baseado na transcript

hello uh and welcome we're here to talk at cubec con EU 2024 about how kubernetes is finally finally removing incl yeah saying words is hard why don't you say the words removing the intrig cloud providers say that three times fast or just try to do it and you'll uh be on this journey with us okay I'm Chris priver uh I'm a software engineer over at equinex I work in the developer relations section um doing Integrations engineering hooking up kubernetes and other things to our apis I'm

### Excerpt da transcript

hello uh and welcome we're here to talk at cubec con EU 2024 about how kubernetes is finally finally removing incl yeah saying words is hard why don't you say the words removing the intrig cloud providers say that three times fast or just try to do it and you'll uh be on this journey with us okay I'm Chris priver uh I'm a software engineer over at equinex I work in the developer relations section um doing Integrations engineering hooking up kubernetes and other things to our apis I'm a ex Kates user I've been there done sisadmin done storage um been in the Kate's ecosystem for I don't know five years uh you can find me on GitHub there's my name c priver excellent uh I'm Bridget cromhout and I'm in product at Microsoft uh I focus on the Upstream open source ecosystem kubernetes web web assembly and all of the fun things and I've been in the kubernetes ecosystem about 7 years now uh and I'm Bridget kod on GitHub all right so we have three things we're going to kind of talk about today we're going to do a quick overview of what exactly do we mean when we're saying cloud provider because I think that's one of those semantically overburdened terms that you know it's like everything is a cloud provider and so we're fig we're going to help you figure out what is then we're going to talk about this migration of in tree to AIT tree and then we're going to give you a few actionable takeaways that you can take and use even if you're not actually making a cloud provider or doing this transition all right so let's see should we start with what is a cloud provider well as you mentioned it's an overloaded term so it we're not referring to here the cloud providers like Azure and Google and you know equinex metal but here we're talking about two things the specific cloud provider infrastructure manager component used by like Azure or equinex metal um like cloud provider equinex metal cloud provider Azure cloud provider Google and then the second part is the cloud controller manager which is kind of the shared component that all those individual vendor ones use so for this talk we're mostly focusing on that shared component so when we say cloud provider referencing the cloud controller manager and its related code yeah and you will see the term cloud provider used elsewhere in kubernetes um in like say s cluster life cycle and the cluster API World Etc so we're not exactly the same as those usages so don't worry too much about that just be aware that you may see that term a
