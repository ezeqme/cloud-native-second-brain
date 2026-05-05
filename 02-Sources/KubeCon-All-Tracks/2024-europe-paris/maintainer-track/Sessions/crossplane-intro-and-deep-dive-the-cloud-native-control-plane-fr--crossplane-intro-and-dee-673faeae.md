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
themes: ["AI ML", "Community Governance"]
speakers: ["Jared Watts", "Philippe Scorsolini", "Upbound"]
sched_url: https://kccnceu2024.sched.com/event/1Yhfi/crossplane-intro-and-deep-dive-the-cloud-native-control-plane-framework-jared-watts-philippe-scorsolini-upbound
youtube_search_url: https://www.youtube.com/results?search_query=Crossplane+Intro+and+Deep+Dive+-+the+Cloud+Native+Control+Plane+Framework+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Crossplane Intro and Deep Dive - the Cloud Native Control Plane Framework - Jared Watts & Philippe Scorsolini, Upbound

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: Jared Watts, Philippe Scorsolini, Upbound
- Schedule: https://kccnceu2024.sched.com/event/1Yhfi/crossplane-intro-and-deep-dive-the-cloud-native-control-plane-framework-jared-watts-philippe-scorsolini-upbound
- Busca YouTube: https://www.youtube.com/results?search_query=Crossplane+Intro+and+Deep+Dive+-+the+Cloud+Native+Control+Plane+Framework+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Crossplane Intro and Deep Dive - the Cloud Native Control Plane Framework.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1Yhfi/crossplane-intro-and-deep-dive-the-cloud-native-control-plane-framework-jared-watts-philippe-scorsolini-upbound
- YouTube search: https://www.youtube.com/results?search_query=Crossplane+Intro+and+Deep+Dive+-+the+Cloud+Native+Control+Plane+Framework+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=S2BQz-5cboA
- YouTube title: Crossplane Intro and Deep Dive - the Cloud Native Control Plane Framework
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/crossplane-intro-and-deep-dive-the-cloud-native-control-plane-framewor/S2BQz-5cboA.txt
- Transcript chars: 31693
- Keywords: crossplane, composition, actually, resources, functions, function, resource, platform, control, environment, write, database, basically, cluster, create, define, providers, engineer

### Resumo baseado na transcript

all right let's get this talk started here right you all are here to listen about crossplane so let's get the crossplane maintainer track talk going so my name is Jared this is Philipe over here and we are both very involved in the crossplane project so this is always an interesting talk because we tried to have something for everybody we try to have some intro material we try to like dive deeper into some topics so we want to have something for everybody so quick show of hands

### Excerpt da transcript

all right let's get this talk started here right you all are here to listen about crossplane so let's get the crossplane maintainer track talk going so my name is Jared this is Philipe over here and we are both very involved in the crossplane project so this is always an interesting talk because we tried to have something for everybody we try to have some intro material we try to like dive deeper into some topics so we want to have something for everybody so quick show of hands who has never used crossplane before ever awesome this slide is for you what is crossplane so crossplane is your Cloud native control plane you can use it to manage all of your resources you can compose those resources into like higher level abstractions and then offer those to your developers so that they could provision infrastructure when they need it kubernetes awesome control plane really really good for containers but crossplane goes and teaches it how to manage like everything else basically control planes are not A New Concept right Cloud providers have been using control control planes for years so it's not a New Concept but now it's your turn to build your own control plane using crossplane so we've been doing this for a bit we we've been around for a little bit over 5 years now uh and we now have a official formal proposal to graduate with the cncf uh so one of the things that really hit me hard when we were pulling together the proposal is how many people have gotten involved in the project so almost 2,000 people have contributed to the project in some way now which is Absol absolutely amazing we're in the top 10% of uh of all cncf projects for people that are writing code for it almost 700 people have written code for crossplane which just blows my mind it's amazing almost 350 companies have contributed something to crossplane too so this community is getting bigger uh the company the the project is mature um it's it's amazing to see this growth um and obviously lots of people are using it right so there it's it's in use in production at scale by lots of companies that you may recognize as well okay so back to the basics for folks so manage resources key Concept in crossplane so every resource out there in the cloud that say AWS there is a crossplane resource to represent it so all the you know 900 I don't know more than that Services AWS has there's a crossplane managed resource for basically all of them so each managed resource is exposed in the kubernetes API as an o
