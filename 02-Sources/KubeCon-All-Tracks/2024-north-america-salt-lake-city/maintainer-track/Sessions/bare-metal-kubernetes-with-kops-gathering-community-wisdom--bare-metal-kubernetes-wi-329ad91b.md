---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Maintainer Track"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Justin Santa Barbara", "Google", "Ciprian Hacman", "Microsoft"]
sched_url: https://kccncna2024.sched.com/event/1howo/bare-metal-kubernetes-with-kops-gathering-community-wisdom-justin-santa-barbara-google-ciprian-hacman-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Bare+Metal+Kubernetes+with+KOps%3A+Gathering+Community+Wisdom+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Bare Metal Kubernetes with KOps: Gathering Community Wisdom - Justin Santa Barbara, Google & Ciprian Hacman, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Justin Santa Barbara, Google, Ciprian Hacman, Microsoft
- Schedule: https://kccncna2024.sched.com/event/1howo/bare-metal-kubernetes-with-kops-gathering-community-wisdom-justin-santa-barbara-google-ciprian-hacman-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Bare+Metal+Kubernetes+with+KOps%3A+Gathering+Community+Wisdom+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Bare Metal Kubernetes with KOps: Gathering Community Wisdom.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1howo/bare-metal-kubernetes-with-kops-gathering-community-wisdom-justin-santa-barbara-google-ciprian-hacman-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Bare+Metal+Kubernetes+with+KOps%3A+Gathering+Community+Wisdom+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=UIO3duG-AXs
- YouTube title: Bare Metal Kubernetes with KOps: Gathering Community Wisdom - Justin Santa Barbara & Ciprian Hacman
- Match score: 0.843
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/bare-metal-kubernetes-with-kops-gathering-community-wisdom/UIO3duG-AXs.txt
- Transcript chars: 25888
- Keywords: anyone, addresses, storage, cluster, basically, server, balancer, running, little, static, actually, network, topics, already, configuration, dependency, probably, machines

### Resumo baseado na transcript

my name is cyprian Hackman I'm a software engineer at Microsoft I work on an internal platform so related to things like this um I'm also a maintainer for various projects inside the kubernetes ecosystem um and uh usually do talks with Justin on such topics hi there my name is uh Justin santabarbara I am a software engineer at Google I've been in the kubernetes ecosystem for a long time uh also involved a number of projects but um primarily CPR and I work together on the chops project

### Excerpt da transcript

my name is cyprian Hackman I'm a software engineer at Microsoft I work on an internal platform so related to things like this um I'm also a maintainer for various projects inside the kubernetes ecosystem um and uh usually do talks with Justin on such topics hi there my name is uh Justin santabarbara I am a software engineer at Google I've been in the kubernetes ecosystem for a long time uh also involved a number of projects but um primarily CPR and I work together on the chops project um we've been adding bare metal support uh to that um but we've also discovered this is a broader topic and so we want to talk about it with you um don't worry this is not the last slide uh but we did put it in here um this is a maintainer track talk and we do you know so we're not going to stand up here for 25 minutes or 30 minutes and lecture you about you know everything we've been building and how it's the only one true way uh we want to find out you know what are you doing what would you like to see uh whether it's in chops or cluster API or in the kubernetes project itself so that it lands in eks AKs gke whatever it is you know just the whole topic um obviously you know metal is not necessarily going to land in gke but we can least talk about those sorts of things so thank you in advance for your participation we will be roaming through the audience so please have your speaking hats on uh and be ready to participate okay so quick survey what is metal so which one of you use kubernetes on metal so okay nice quite a lot of hands so what is metal for you right it's a it's a very controversial topic could be your own machine in your data centers could be collocated data center could be also a cloud providers instances that you're not using some managed product or the cloud part so how do you how do you think about the cloud anyone I can go first I I for example I'm running a handful of um of machines physical machines in my basement at home uh in the winter months it keeps warm um and I would like to run kubernetes on those it's it's about five machines right now and growing but I also you know I'm playing with AI so gpus are a big thing for for me I said Cloud equal easy world so basically on bare metal you have a lot of stuff to do to to deliver your kubernetes on it in the cloud not in Cloud you already have all solution around it so how easy how easy can we make it right I think that's a great one and we're going to talk a lot about the challenges um anyone else want to
