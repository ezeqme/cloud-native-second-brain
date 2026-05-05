---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Maintainer Track"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Michael McCune", "Joel Speed", "Red Hat", "Bridget Kromhout", "Microsoft"]
sched_url: https://kccnceu2023.sched.com/event/1Hzci/the-ins-and-outs-of-the-cloud-provider-in-kubernetes-michael-mccune-joel-speed-red-hat-bridget-kromhout-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=The+Ins+and+Outs+of+the+Cloud+Provider+in+Kubernetes+CNCF+KubeCon+2023
slides: []
status: parsed
---

# The Ins and Outs of the Cloud Provider in Kubernetes - Michael McCune & Joel Speed, Red Hat & Bridget Kromhout, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Michael McCune, Joel Speed, Red Hat, Bridget Kromhout, Microsoft
- Schedule: https://kccnceu2023.sched.com/event/1Hzci/the-ins-and-outs-of-the-cloud-provider-in-kubernetes-michael-mccune-joel-speed-red-hat-bridget-kromhout-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=The+Ins+and+Outs+of+the+Cloud+Provider+in+Kubernetes+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre The Ins and Outs of the Cloud Provider in Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1Hzci/the-ins-and-outs-of-the-cloud-provider-in-kubernetes-michael-mccune-joel-speed-red-hat-bridget-kromhout-microsoft
- YouTube search: https://www.youtube.com/results?search_query=The+Ins+and+Outs+of+the+Cloud+Provider+in+Kubernetes+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=i2dNGzB0PMI
- YouTube title: The Ins & Outs of the Cloud Provider in Kubernetes - Michael McCune & Joel Speed & Bridget Kromhout
- Match score: 0.751
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/the-ins-and-outs-of-the-cloud-provider-in-kubernetes/i2dNGzB0PMI.txt
- Transcript chars: 36617
- Keywords: provider, providers, controller, interface, instances, probably, actually, looking, cluster, talking, balancer, running, information, working, infrastructure, available, issues, important

### Resumo baseado na transcript

welcome welcome to the Sig Cloud prep wow saying words is hard let's try that again welcome to the Sig cloud provider update for kubecon EU 2023 this is super exciting we have a packed room we have a packed agenda we have a pack stage let's get into it I'm Bridget crumhout I work at Microsoft Azure and uh I've been working in the kubernetes space for it seems like 800 000 years but I think some of those are pandemic use which are either shorter or longer not

### Excerpt da transcript

welcome welcome to the Sig Cloud prep wow saying words is hard let's try that again welcome to the Sig cloud provider update for kubecon EU 2023 this is super exciting we have a packed room we have a packed agenda we have a pack stage let's get into it I'm Bridget crumhout I work at Microsoft Azure and uh I've been working in the kubernetes space for it seems like 800 000 years but I think some of those are pandemic use which are either shorter or longer not really sure um what did I promise I promised something probably ah yes um I am very interested in hearing what all of you are doing with your hybrid Cloud which someone just reminded me this morning actually exists right yeah uh I'm Michael McKeon I'm a software engineer at Red Hat uh mainly working on cloud infrastructure and auto scaling and all those kind of fun things uh yeah I've been working on kubernetes for you know more than a few years and um yeah just here to have some fun of Joel speed I work for Red Hat as part of openshift working on the cloud infrastructure stuff I started with Cube about six years ago as an SRE and then at some point decided to go into software uh and yeah that's kind of how I ended up in cloud I was on call until 2015 and at that point I was like I probably should let someone else be on call like people like Jewel why not yeah I mean that's one of the reasons I moved into software was to avoid uncall okay all right um where are where can I not we didn't assign who's going to set the foundation all right cloud provider it's important clearly you think so let's get into it the problem is I'm having difficulty seeing so I'm going to be that person who looks like this and say ah yes so cloud provider might mean different things to different people I need to actually be able to see something unfortunately to see which slide I'm on I'm sorry uh yes it mostly refers to the infrastructure it's deployed on but it actually also refers to very specific software bits and there's a lot of disambiguation that we kind of have to do in this space so hopefully that helps uh yeah so like the the important thing to remember here is that you know cloud provider can mean a couple different things right and so people use it generically but what we're going to dive into here are some of the terms that you're going to want to know when you're looking at the cloud provider that we call you know the component inside of kubernetes so just a couple definitions uh KCM uh many of you are probably f
