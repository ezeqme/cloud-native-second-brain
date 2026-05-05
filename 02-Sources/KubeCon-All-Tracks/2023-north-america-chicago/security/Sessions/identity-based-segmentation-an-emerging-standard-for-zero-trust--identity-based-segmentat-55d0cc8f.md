---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Security"
themes: ["Security"]
speakers: ["Zack Butcher", "Tetrate"]
sched_url: https://kccncna2023.sched.com/event/1R2qp/identity-based-segmentation-an-emerging-standard-for-zero-trust-from-nist-zack-butcher-tetrate
youtube_search_url: https://www.youtube.com/results?search_query=Identity-Based+Segmentation%3A+An+Emerging+Standard+for+Zero+Trust+from+NIST+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Identity-Based Segmentation: An Emerging Standard for Zero Trust from NIST - Zack Butcher, Tetrate

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Security]]
- Temas: [[Security]]
- País/cidade: United States / Chicago
- Speakers: Zack Butcher, Tetrate
- Schedule: https://kccncna2023.sched.com/event/1R2qp/identity-based-segmentation-an-emerging-standard-for-zero-trust-from-nist-zack-butcher-tetrate
- Busca YouTube: https://www.youtube.com/results?search_query=Identity-Based+Segmentation%3A+An+Emerging+Standard+for+Zero+Trust+from+NIST+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Identity-Based Segmentation: An Emerging Standard for Zero Trust from NIST.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2qp/identity-based-segmentation-an-emerging-standard-for-zero-trust-from-nist-zack-butcher-tetrate
- YouTube search: https://www.youtube.com/results?search_query=Identity-Based+Segmentation%3A+An+Emerging+Standard+for+Zero+Trust+from+NIST+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=XE6Q7kwptwo
- YouTube title: Identity-Based Segmentation: An Emerging Standard for Zero Trust from NIST - Zack Butcher, Tetrate
- Match score: 0.954
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/identity-based-segmentation-an-emerging-standard-for-zero-trust-from-n/XE6Q7kwptwo.txt
- Transcript chars: 35527
- Keywords: identity, policy, network, access, segmentation, mesh, actually, context, authenticate, encryption, policies, implement, request, little, security, attacker, similar, application

### Resumo baseado na transcript

uh everybody welcome thank you for coming today uh hopefully we're going to have a pretty good talk uh about uh some really you know fascinating riveting stuff arest standards uh but hopefully this will be this will be some good good material for everybody so a couple you I kind of lied a little bit the title is a little bit of a misnomer uh I mean I guess technically the standard is emerging but but it has emerged it's been published uh the final paper is out um

### Excerpt da transcript

uh everybody welcome thank you for coming today uh hopefully we're going to have a pretty good talk uh about uh some really you know fascinating riveting stuff arest standards uh but hopefully this will be this will be some good good material for everybody so a couple you I kind of lied a little bit the title is a little bit of a misnomer uh I mean I guess technically the standard is emerging but but it has emerged it's been published uh the final paper is out um and actually we don't write standards at this uh we write guidelines uh other folks write standards based on the guidelines uh but this is now our our published uh guidelines for zero trust and specifically uh 800 207a is focused on uh runtime uh zero trust so uh before I di in a little bit about me uh I'm Zach uh founding engineer at tetrate uh I was one of the early Engineers on the iso project and I worked across Google Cloud before then uh on things like the project Service uh on stuff like ID and access management on our service mesh and then ultimately on ISO uh the other big hat that I wear these days is doing research uh as well as writing standards uh or guidelines uh withness uh on microservice security on zero trust and on access control so with that today uh the first thing I want to equip youall with is a working definition of zero trust I think there's a lot of fud in the space around what zero trust is or isn't and so we want to get to the bottom of that and have a a real concrete definition as part of that I'm going to introduce identity based segmentation that's the primary uh idea that we uh brought out in 207a if there's one thing that you take away from The Talk today take away identity based segmentation um we're going to talk about then how we can start to move incrementally from where we are today into an identity based model maybe eventually realize identity based segmentation and then finally I'll spend a little bit of time talking about one of the ways that you can choose to implement this uh which would be a with a service mesh so first and foremost let's let's start to Define zero trust uh I actually hate the name uh we really it should be about zero implicit trust right the the problem is not trust the problem is when we it's not made explicit so we don't necessarily know what access is happening or we're not authorizing it authenticating it and doing a couple other things I'll talk about so what are some different ways to think about zero trust one of the framings tha
