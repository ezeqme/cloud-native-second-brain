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
themes: ["AI ML", "Community Governance"]
speakers: ["Jared Watts", "Mark Anderson-Trocme", "Upbound"]
sched_url: https://kccncna2024.sched.com/event/1hoxu/crossplane-intro-and-deep-dive-the-cloud-native-control-plane-framework-jared-watts-mark-anderson-trocme-upbound
youtube_search_url: https://www.youtube.com/results?search_query=Crossplane+Intro+and+Deep+Dive+-+The+Cloud+Native+Control+Plane+Framework+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Crossplane Intro and Deep Dive - The Cloud Native Control Plane Framework - Jared Watts & Mark Anderson-Trocme, Upbound

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Jared Watts, Mark Anderson-Trocme, Upbound
- Schedule: https://kccncna2024.sched.com/event/1hoxu/crossplane-intro-and-deep-dive-the-cloud-native-control-plane-framework-jared-watts-mark-anderson-trocme-upbound
- Busca YouTube: https://www.youtube.com/results?search_query=Crossplane+Intro+and+Deep+Dive+-+The+Cloud+Native+Control+Plane+Framework+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Crossplane Intro and Deep Dive - The Cloud Native Control Plane Framework.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1hoxu/crossplane-intro-and-deep-dive-the-cloud-native-control-plane-framework-jared-watts-mark-anderson-trocme-upbound
- YouTube search: https://www.youtube.com/results?search_query=Crossplane+Intro+and+Deep+Dive+-+The+Cloud+Native+Control+Plane+Framework+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=9orgZBxCQhc
- YouTube title: Crossplane Intro and Deep Dive - The Cloud Native Control Plane Fram... J. Watts, M. Anderson-Trocme
- Match score: 0.927
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/crossplane-intro-and-deep-dive-the-cloud-native-control-plane-framewor/9orgZBxCQhc.txt
- Transcript chars: 39272
- Keywords: crossplane, resources, config, basically, terraform, provider, function, control, developers, infrastructure, platform, developer, functions, environment, whatever, create, little, object

### Resumo baseado na transcript

all right so we are going to talk about the crossplane project my name is Jared I'm one of the creators of the project and I have here my friend Mark who has built multiple uh platforms and control planes on uh crossplane that are all running in production so uh you can consider him a bit of an expert on the topic as well um as is usual for this session here we always have a fairly diverse set of uh folks in terms of level of experience and

### Excerpt da transcript

all right so we are going to talk about the crossplane project my name is Jared I'm one of the creators of the project and I have here my friend Mark who has built multiple uh platforms and control planes on uh crossplane that are all running in production so uh you can consider him a bit of an expert on the topic as well um as is usual for this session here we always have a fairly diverse set of uh folks in terms of level of experience and familiarity with crossplane so we're going to have you know kind of something for everybody really so we're going to have we have to start with some intro material for folks that don't really know what crossplane is but then after about 10 minutes or so we're going to get into a little bit of a deeper dive we're going to be showing off new features and new demos and stuff like that so there will be something for everybody but first we got to start with the basics so for folks that don't know cross plane we can consider it your Cloud native control plane it basically helps you provision and manage everything all your resources so you can take those resources you can compose them into higher level abstractions and then you can then expose those abstractions to your developers in order for them to be able to selfservice and get the uh infrastructure and resources that they need when they need it in in a safe manner so kubernetes uh it is a great control plane it does great things for containers basically cross plane comes into kubernetes extends it and then teaches it how to be a great control plane for everything else Beyond containers um and then control planes Not A New Concept we didn't invent control planes right Cloud providers have been using them for years to manage their backend systems and so now cross planes here to help help you build your own control plane as well so we are a cncf project right this is the maintainer track talk uh we know donated to the the project uh to the cncf like three four years ago or so um I've said this before but we are ready for graduation I think we opened the proposal to graduate back in February so it's been a few months that we've been waiting to go through the process it's a bit of a patience a game of patience if you will but the key takeaway to this slide here is just how many people are involved in the project right we've got thousands of people contributing to it in some way and we have a lot of really impressive adopters of the project too so lots of people are coming toge
