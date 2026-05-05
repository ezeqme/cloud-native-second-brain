---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Operations + Performance"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Roman Doroschevici", "Sian Meoli", "Google"]
sched_url: https://kccnceu2024.sched.com/event/1YeS3/kubernetes-chronicles-stories-of-triumph-in-kubernetes-support-roman-doroschevici-sian-meoli-google
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+Chronicles%3A+Stories+of+Triumph+in+Kubernetes+Support+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Kubernetes Chronicles: Stories of Triumph in Kubernetes Support - Roman Doroschevici & Sian Meoli, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: France / Paris
- Speakers: Roman Doroschevici, Sian Meoli, Google
- Schedule: https://kccnceu2024.sched.com/event/1YeS3/kubernetes-chronicles-stories-of-triumph-in-kubernetes-support-roman-doroschevici-sian-meoli-google
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+Chronicles%3A+Stories+of+Triumph+in+Kubernetes+Support+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Kubernetes Chronicles: Stories of Triumph in Kubernetes Support.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeS3/kubernetes-chronicles-stories-of-triumph-in-kubernetes-support-roman-doroschevici-sian-meoli-google
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+Chronicles%3A+Stories+of+Triumph+in+Kubernetes+Support+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=IW46dt_JrE4
- YouTube title: Kubernetes Chronicles: Stories of Triumph in Kubernetes Support - Roman Doroschevici & Sian Meoli
- Match score: 0.885
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/kubernetes-chronicles-stories-of-triumph-in-kubernetes-support/IW46dt_JrE4.txt
- Transcript chars: 24288
- Keywords: cluster, config, certificate, server, logs, working, customer, actually, everything, support, create, running, message, request, issues, understand, happening, trying

### Resumo baseado na transcript

okay I'm I'm going to start so hello hello everybody and welcome to our show uh sorry to our talk my name is Roman and I'm a Technical Solutions engineer at Google today I'm going to be talking about kubernetes support at Google Cloud uh I just said that I'm Technical Solutions engineer but that's just a fancy name for a support engineer so why we are all here we all know that kubernetes is a powerful container orry we are all here that's why we are here and kubernetes gatekeeper Dosh and we can also confirm here it has a timeout of 3 seconds which we saw in the logs and we see here a failure policy of fail and again back to documentation we're curious to understand what is a failure policy of

### Excerpt da transcript

okay I'm I'm going to start so hello hello everybody and welcome to our show uh sorry to our talk my name is Roman and I'm a Technical Solutions engineer at Google today I'm going to be talking about kubernetes support at Google Cloud uh I just said that I'm Technical Solutions engineer but that's just a fancy name for a support engineer so why we are all here we all know that kubernetes is a powerful container orry we are all here that's why we are here and kubernetes is turning 10 years this year we all know that the first cubec con was almost 9 years ago after all this time we are all long past the demos all long past the PC's many of you already adopted kubernetes and using it in production and um but with all the all of the Ben that's all due to benefits kubernetes brings but with all of the benefits there also come the challenges let's face it kubernetes is not a magic want it also needs some loves and attention but fear not that's where people like me and my colleagues come in to save the day let's take a look at some Trends out of all the cases kubernetes related cases received in 2023 here is the list of future cases by Future in descending on or order uh this is not an exhaustive list but these are just the top seven features if we take a look at this list at the first place is networking and it makes sense one of the main use cases of kubernetes are microservices and all those microservices need to chat as a result first place is networking node related issues are usually related to node stability resource allocation or node failures if if kubernetes has like Auto healing mechanisms and it reschedules the workload it replaces the failed node what I noticed is that people really care about what happens to that node and they really want to know why they failed for control plane issues we are dealing with Qi server controller manager atcd these issues usually do not affect the workload directly but they do affect the scheduling part the orchestration part so they do get your attention really quickly even if your control plane is managed by a service provider you can still break it depending on what you're running in your cluster all those control plane components they don't have infinite resources so for example if you have a controller that runs and creates only resources and doesn't delete them you can easily fill out the itd database causing issues another way to look at this list is uh which feature is the most popular and the most complicated
