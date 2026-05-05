---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Community Governance"]
speakers: ["Travis Nielsen", "Sebastien Han", "Blaine Gardner", "Red Hat", "Satoru Takeuchi", "Cybozu", "Inc"]
sched_url: https://kccncna2021.sched.com/event/lV6w/rook-intro-and-ceph-deep-dive-travis-nielsen-sebastien-han-blaine-gardner-red-hat-satoru-takeuchi-cybozu-inc
youtube_search_url: https://www.youtube.com/results?search_query=Rook%3A+Intro+and+Ceph+Deep+Dive+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Rook: Intro and Ceph Deep Dive - Travis Nielsen, Sebastien Han & Blaine Gardner, Red Hat; Satoru Takeuchi, Cybozu, Inc

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Los Angeles
- Speakers: Travis Nielsen, Sebastien Han, Blaine Gardner, Red Hat, Satoru Takeuchi, Cybozu, Inc
- Schedule: https://kccncna2021.sched.com/event/lV6w/rook-intro-and-ceph-deep-dive-travis-nielsen-sebastien-han-blaine-gardner-red-hat-satoru-takeuchi-cybozu-inc
- Busca YouTube: https://www.youtube.com/results?search_query=Rook%3A+Intro+and+Ceph+Deep+Dive+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Rook: Intro and Ceph Deep Dive.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV6w/rook-intro-and-ceph-deep-dive-travis-nielsen-sebastien-han-blaine-gardner-red-hat-satoru-takeuchi-cybozu-inc
- YouTube search: https://www.youtube.com/results?search_query=Rook%3A+Intro+and+Ceph+Deep+Dive+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=bL5Ay28KPOI
- YouTube title: Rook: Intro and Deep Dive with Ceph
- Match score: 0.842
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/rook-intro-and-ceph-deep-dive/bL5Ay28KPOI.txt
- Transcript chars: 26938
- Keywords: cluster, actually, storage, upgrade, basically, fellow, domain, application, backup, encryption, always, volume, support, sometimes, restore, features, especially, already

### Resumo baseado na transcript

hello everyone Welcome to The Rook intro and deep di with SEF talk I'm here with bla yeah I'm blae Gardner I'm a storage engineer at IBM and Rec maintainer hello I'm I'm SEF and open shap data Foundation which is work and St and lots of cool stuff in open shift at IBM architect at IBM M and I'm JC Lopez so I do uh pre-sales and Consulting and whatever you want around RF and anything containers related to storage so and really quick to myself I'm also maintain support um something that's dear to me is uh object storage provisioning so Rook was an early investor in um self-service provisioning of object storage buckets um so this was done with a project that uh provided object bucket claims uh and this was like back in 2019 and that evolved into a uh kuat enhancement project now which we're uh helping to try to like Usher into beta uh which is uh uh this cozy project the container object storage interface to allow a little bit more flexibility there

### Excerpt da transcript

hello everyone Welcome to The Rook intro and deep di with SEF talk I'm here with bla yeah I'm blae Gardner I'm a storage engineer at IBM and Rec maintainer hello I'm I'm SEF and open shap data Foundation which is work and St and lots of cool stuff in open shift at IBM architect at IBM M and I'm JC Lopez so I do uh pre-sales and Consulting and whatever you want around RF and anything containers related to storage so and really quick to myself I'm also maintain of The Rook project and um working for C Technologies in ging engineer okay so what do we want to talk about today in The Rook intro and deep dive we want to give you an introduction to rook and SE for anyone who's new we want to talk about the state of The Rook project what's in the making any cool features we have cooking up and some real life example and additionally which I think is interesting for a lot of people also the newcomers to Rook is application disaster recovery and especially also day two because second day operations well first day it works second day it's uh broken we don't want wanted so let's talk about it so first of all a few questions um who's here to learn about Rook for the first time quite quite a few people has anyone of you already experimented with Rook okay and who has Rook deployed in production but like I guess we can see production is a bit of a stretchy term even like in test environment okay and question which is not on the slide um where do you run Rook do you run it on uh in the cloud in a virtualized environment on Prem okay on bare metal on Prem then few more people okay on Prim and bare metal okay um yeah let's talk about Rook yeah that's you um yeah to get us started I want to talk talk about just kind of an introduction to Rook starting from the very beginning what are the questions that led to Rook um so in a in a cloud world where Cloud providers are usually providing storage what you do in your own Data Center and also like why you know what storage is normally part of uh uh or like not part of the kubernetes cluster but why why can't it be in the kubernetes cluster for the kubernetes cluster and then managed in the same way as kubernetes applications so these questions and some iteration led us to some goals for rook and so that's make storage available to kubernetes applications and have them be kubernetes native um just like the storage that you would get from cloud vendors and we also want to make that easy um so automating the deployment configuration
