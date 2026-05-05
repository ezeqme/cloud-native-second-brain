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
themes: ["Kubernetes Core"]
speakers: []
sched_url: https://kccnceu2024.sched.com/event/1aQWQ/monitoring-kubernetes-and-cloud-spend-with-opencost-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=Monitoring+Kubernetes+and+Cloud+Spend+with+OpenCost+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Monitoring Kubernetes and Cloud Spend with OpenCost | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: N/A
- Schedule: https://kccnceu2024.sched.com/event/1aQWQ/monitoring-kubernetes-and-cloud-spend-with-opencost-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=Monitoring+Kubernetes+and+Cloud+Spend+with+OpenCost+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Monitoring Kubernetes and Cloud Spend with OpenCost | Project Lightning Talk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1aQWQ/monitoring-kubernetes-and-cloud-spend-with-opencost-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=Monitoring+Kubernetes+and+Cloud+Spend+with+OpenCost+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=OQzZcHXL_7o
- YouTube title: Monitoring Kubernetes and Cloud Spend with OpenCost | Project Lightning Talk
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/monitoring-kubernetes-and-cloud-spend-with-opencost-project-lightning/OQzZcHXL_7o.txt
- Transcript chars: 6646
- Keywords: cost, carbon, access, prometheus, source, pretty, footprint, release, allows, monitoring, specification, implementation, github, started, ability, whatever, available, everything

### Resumo baseado na transcript

hi I'm Matt Ray I'm the uh the open cost Community manager and I work for CP cost um so I'm here to talk about open cost open cost is the open source kubernetes and Cloud cost monitoring project uh we are both a specification and an implementation so I'll talk about that in a second uh but what's important to note is we are a cncf Sandbox project and uh we are also the only cncf and FNAF certified solution so we're at that nice section of cncf fops 108 we introduced Cloud cost and so this is as far as I know uh the first implement the first open source implementation of going and processing your your AWS gcp and is your cost and usage reports so if you're familiar with Cloud billing um your Cloud providers are pushing out a huge amount of Json or csvs or uh you know whatever it might be of how you're actually spending your Cloud cost these are large and complex I mean I've seen terabyte siiz files from uh some of the customers Cloud cost gives you the ability to parse those and actually put an API in front of them for reporting so if uh that's a new feature as far as I know not available anywhere else um it's not tied to your kubernetes cost just yet so you have your kubernetes cost allocation your Cloud cost the carbon costs are going to be next to uh your kubernetes cost and your Cloud cost and the open cost plugins we're going to let you mix and match where

### Excerpt da transcript

hi I'm Matt Ray I'm the uh the open cost Community manager and I work for CP cost um so I'm here to talk about open cost open cost is the open source kubernetes and Cloud cost monitoring project uh we are both a specification and an implementation so I'll talk about that in a second uh but what's important to note is we are a cncf Sandbox project and uh we are also the only cncf and FNAF certified solution so we're at that nice section of cncf fops Open Source and uh all that goodness um there's our website our GitHub and uh our link on the cncf site so open cost started uh we joined the cncf in June of 2022 uh we started as a specification a a bunch of smart kubernetes folks uh got together from different organizations AWS Red Hat uh gcp um coup cost and they got together and determined like this is how we should measure how costs are allocated in kubernetes so on the left you have the things that you get from uh from your uh cloud provider and what you get from the node itself you know how much CPU how much memory how much GPU is taken by your workloads and then on the right is how you can split that up so you can say hey I want to see uh you know all the cost of all my applications per namespace or I could do multi- agregation I want to see per namespace um with you know the pods in each Nam space uh so we give you a lot of flexibility can also do tags and labels of course um but really you can slice and dice your kubernetes data pretty much any way you want and so that's the specification talks about how things are shared equally uh but it also talks about you know how to to to record all these things and so that's how Opus got started Focus strictly on kubernetes uh but today uh I'm excited to announce that uh this week uh we're going to be uh releasing carbon cost that is a new feature we're going to be bringing in um the ability to measure the carbon footprint of your uh of your workloads um it's still pretty rough uh a work in progress thank you I didn't write it but I'm happy I'm happy about it uh it's based off the The Open Source uh carbon uh the uh Cloud carbon footprint project so CCF uh Cloud carbon footprint.

org uh we've been working with the fine folks over at thought works on that and so we're going to be the codes in Mainline uh we'll have it out in our next release maybe this week maybe next week but we're working on that uh we're also going to be announcing this week that uh we have a new plug-in architecture and what this new plug-in
