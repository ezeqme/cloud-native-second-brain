---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "101 Track"
themes: ["101 Track"]
speakers: ["Jussi Nummelin", "Mirantis Inc."]
sched_url: https://kccnceu2021.sched.com/event/iE4h/what-do-you-mean-k8s-doesnt-have-users-how-do-i-manage-user-access-then-jussi-nummelin-mirantis-inc
youtube_search_url: https://www.youtube.com/results?search_query=What+Do+You+Mean+K8s+Doesn%27t+Have+Users%3F+How+Do+I+Manage+User+Access+Then%3F+CNCF+KubeCon+2021
slides: []
status: parsed
---

# What Do You Mean K8s Doesn't Have Users? How Do I Manage User Access Then? - Jussi Nummelin, Mirantis Inc.

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[101 Track]]
- Temas: [[101 Track]]
- País/cidade: Virtual / Virtual
- Speakers: Jussi Nummelin, Mirantis Inc.
- Schedule: https://kccnceu2021.sched.com/event/iE4h/what-do-you-mean-k8s-doesnt-have-users-how-do-i-manage-user-access-then-jussi-nummelin-mirantis-inc
- Busca YouTube: https://www.youtube.com/results?search_query=What+Do+You+Mean+K8s+Doesn%27t+Have+Users%3F+How+Do+I+Manage+User+Access+Then%3F+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre What Do You Mean K8s Doesn't Have Users? How Do I Manage User Access Then?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE4h/what-do-you-mean-k8s-doesnt-have-users-how-do-i-manage-user-access-then-jussi-nummelin-mirantis-inc
- YouTube search: https://www.youtube.com/results?search_query=What+Do+You+Mean+K8s+Doesn%27t+Have+Users%3F+How+Do+I+Manage+User+Access+Then%3F+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_Dzc07aBQHI
- YouTube title: What Do You Mean K8s Doesn't Have Users? How Do I Manage User Access Then? - Jussi Nummelin
- Match score: 0.984
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/what-do-you-mean-k8s-doesnt-have-users-how-do-i-manage-user-access-the/_Dzc07aBQHI.txt
- Transcript chars: 20788
- Keywords: server, course, access, information, actually, tokens, basically, external, itself, identity, client, certificates, authentication, control, certificate, create, essentially, cluster

### Resumo baseado na transcript

uh welcome to talk a bit on the user management in in kubernetes or well as that as the title of the talk says it's more like a lack of user user management capabilities in kubernetes uh the whole talk kind of stems from from uh different different discussions that i've had with with people new or newer into the into the world of kubernetes and and kind of the blood of confusion that that yeah i have now my cluster up and running so how do i how do

### Excerpt da transcript

uh welcome to talk a bit on the user management in in kubernetes or well as that as the title of the talk says it's more like a lack of user user management capabilities in kubernetes uh the whole talk kind of stems from from uh different different discussions that i've had with with people new or newer into the into the world of kubernetes and and kind of the blood of confusion that that yeah i have now my cluster up and running so how do i how do i actually grant access to to another set of users for my my cluster uh so we are at cubecon 2021 and and we're on the 101 track so um we're not gonna dive too deep into the into the whole whole topics and different different configuration options for example uh but but we're uh we are gonna look at the the kind of high level high level um topics and and concepts how do how do you actually then then really manage the access for your users into your your clusters uh so yeah hi i'm i'm yusuf malin working at uh miranda's engineering um i've been working with kubernetes and and different cloud native technologies for the past quite quite a few years even even actually before they were really called like cloud native stuff uh in the past year or so i've been i've been mostly working with uh with the new open source kubernetes distro called k0s and and and and that's basically that the reason why you see some some mentions of it and in the in the examples so so this is not really a topic on case stores itself but but you'll see some examples how we do things in case zeros for example and and of course as i said it's open source so you can you can dig into that if you if you really want uh although not entirely correct but uh the kind of good way to get your mindset into in the correct correct kind of uh uh direction when when when when thinking about this whole users in in kubernetes topic is is like really really kind of realize the fact that that there is no really there's no users in kubernetes or or users managed by kubernetes per se of course there are users using using kubernetes but but uh the kubernetes control plane doesn't really manage manage to user access for you we'll dive into into this soon some of the topics that we are going to look in this session is of course a quick look on on on how to hold authentication authorization and admission control that aaa functionality really kind of works in a high level on the api server uh we are gonna have a look at that what what is the thing that that we we said
