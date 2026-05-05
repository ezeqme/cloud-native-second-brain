---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Unclassified"
themes: ["GitOps Delivery", "Kubernetes Core"]
speakers: ["Dan Garfield", "Brandon Phillips", "Codefresh"]
sched_url: https://kccnceu2023.sched.com/event/1Hybl/unlocking-argo-cds-hidden-tools-for-chaos-engineering-featuring-vcluster-and-more-dan-garfield-brandon-phillips-codefresh
youtube_search_url: https://www.youtube.com/results?search_query=Unlocking+Argo+CD%E2%80%99s+Hidden+Tools+for+Chaos+Engineering+-+Featuring+VCluster+and+More+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Unlocking Argo CD’s Hidden Tools for Chaos Engineering - Featuring VCluster and More - Dan Garfield & Brandon Phillips, Codefresh

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Unclassified]]
- Temas: [[GitOps Delivery]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Dan Garfield, Brandon Phillips, Codefresh
- Schedule: https://kccnceu2023.sched.com/event/1Hybl/unlocking-argo-cds-hidden-tools-for-chaos-engineering-featuring-vcluster-and-more-dan-garfield-brandon-phillips-codefresh
- Busca YouTube: https://www.youtube.com/results?search_query=Unlocking+Argo+CD%E2%80%99s+Hidden+Tools+for+Chaos+Engineering+-+Featuring+VCluster+and+More+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Unlocking Argo CD’s Hidden Tools for Chaos Engineering - Featuring VCluster and More.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1Hybl/unlocking-argo-cds-hidden-tools-for-chaos-engineering-featuring-vcluster-and-more-dan-garfield-brandon-phillips-codefresh
- YouTube search: https://www.youtube.com/results?search_query=Unlocking+Argo+CD%E2%80%99s+Hidden+Tools+for+Chaos+Engineering+-+Featuring+VCluster+and+More+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Z0RB5SFs6fI
- YouTube title: Unlocking Argo CD’s Hidden Tools for Chaos Engineering - Featuring... - D Garfield & B Phillips
- Match score: 0.899
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/unlocking-argo-cds-hidden-tools-for-chaos-engineering-featuring-vclust/Z0RB5SFs6fI.txt
- Transcript chars: 29542
- Keywords: argo, actually, applications, clusters, cluster, pretty, instance, thousand, little, performance, around, working, production, application, basically, objects, probably, question

### Resumo baseado na transcript

I'm an Argo project maintainer though probably the least of the maintainers and I am also a co-creator of the open get Ops project and get Ops working group and underneath the cncf and you can follow me on Twitter at today was awesome I would love to see you on there and if you didn't like this talk please rate me on Twitter if you liked it be sure to tag me yeah and I'm Brandon Phillips I'm a principal technologist and also the head of our technical product

### Excerpt da transcript

I'm an Argo project maintainer though probably the least of the maintainers and I am also a co-creator of the open get Ops project and get Ops working group and underneath the cncf and you can follow me on Twitter at today was awesome I would love to see you on there and if you didn't like this talk please rate me on Twitter if you liked it be sure to tag me yeah and I'm Brandon Phillips I'm a principal technologist and also the head of our technical product marketing at code fresh also the host of emergency domain which is a CI CD webinar and podcast Series so feel free to check us out you can at me at techie overtime on Twitter just a little heads up code fresh itself we are an Enterprise Argo solution we've actually been working with Argo and customers for more than two years now and it's just been an amazing experience yeah thank you Brandon so we're going to be talking about Argo yeah simple yeah how hard could it be right I mean you have your desired State you have your actual State you know following all the get Ops principles we want those to sync up you know utilize our declarative configuration how hard can it really be Dan it's pretty simple right just comparing two things yeah now my question is let's just check with the audience here who's using Argo CD in production today everyone yeah like everyone in the room okay that that is amazing by the way good job uh so Argo itself obviously an amazing project it can be nearly bulletproof but what happens when you start adding lots and lots of kubernetes clusters uh we know that the world is not that simple right yeah you're not going to get away with just having a few clusters linked into it especially as you scale over time you're going to add more and more clusters and what happens if we start to add even more git repos as we know you're not going to have applications without source code repos you're not going to have the Clusters without applications to deploy to the Clusters so you start to grow and grow and grow at what point could this potentially become a problem yeah and uh obviously 10 000 apps with different sync policies different sized repos you know what could possibly go wrong yeah so then the question is is one Argo instance enough um Can it handle everything that your organization needs maybe some of you are already separating out your Argo instances for other reasons but if you're sticking with one Argo instance maybe you're set up in Hub and spoke and you have a lot of clusters tie
