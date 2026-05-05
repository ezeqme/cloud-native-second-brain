---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Application + Development"
themes: ["Application + Development"]
speakers: ["Alex Meijer", "Anusha Iyer", "Corsha", "Inc."]
sched_url: https://kccncna2021.sched.com/event/lV04/cloud-agnostic-design-for-fun-and-profit-alex-meijer-anusha-iyer-corsha-inc
youtube_search_url: https://www.youtube.com/results?search_query=Cloud-Agnostic+Design+for+Fun+and+Profit+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Cloud-Agnostic Design for Fun and Profit - Alex Meijer & Anusha Iyer, Corsha, Inc.

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Application + Development]]
- Temas: [[Application + Development]]
- País/cidade: United States / Los Angeles
- Speakers: Alex Meijer, Anusha Iyer, Corsha, Inc.
- Schedule: https://kccncna2021.sched.com/event/lV04/cloud-agnostic-design-for-fun-and-profit-alex-meijer-anusha-iyer-corsha-inc
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud-Agnostic+Design+for+Fun+and+Profit+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Cloud-Agnostic Design for Fun and Profit.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV04/cloud-agnostic-design-for-fun-and-profit-alex-meijer-anusha-iyer-corsha-inc
- YouTube search: https://www.youtube.com/results?search_query=Cloud-Agnostic+Design+for+Fun+and+Profit+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=OpZQq_zWQA0
- YouTube title: Cloud-Agnostic Design for Fun and Profit - Alex Meijer & Anusha Iyer, Corsha, Inc.
- Match score: 0.776
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/cloud-agnostic-design-for-fun-and-profit/OpZQq_zWQA0.txt
- Transcript chars: 32735
- Keywords: provider, providers, cluster, terraform, little, agnostic, charts, design, platform, distributed, actually, running, customer, question, wanted, startup, course, absolutely

### Resumo baseado na transcript

all right uh we're gonna go ahead and get started now and welcome everybody uh thanks for joining session today uh my name is danielle i'm cncf ambassador and suburban track chair this is kubecon and i'm so glad to be here for moderating this session today so we're going to talk a little bit about the cloud agnostic design for front and profit today and then just one quick remind and then you've got any technical question during the session please raise your hand end of the session and this isn't black and white uh in terms of what you need to stay agnostic with if it's a low-cost service not worth the effort that's fine um you know so there's obviously choices as you're going through this and then definitely you know that dials you can turn so um i guess funny story here when we introduced a modsec waff into our ingress controllers we turned it on in production and i was going through a couple weeks of just a whole bunch of of demos like back to back and you know it's a very stable demo environment never had troubles before all of a sudden the demo gods are just like pouring terror upon me and about every two or three demos unreliably i would start blocking myself like literally get like flagged by modsuck and i realized we didn't realize that was happening time but the demo flow i was generating poor authentication requests and i was triggering the defaults in our modsig...

### Excerpt da transcript

all right uh we're gonna go ahead and get started now and welcome everybody uh thanks for joining session today uh my name is danielle i'm cncf ambassador and suburban track chair this is kubecon and i'm so glad to be here for moderating this session today so we're going to talk a little bit about the cloud agnostic design for front and profit today and then just one quick remind and then you've got any technical question during the session please raise your hand end of the session and our great speakers and presenter will address your questions so now i'm gonna introduce our presenter our alex meyer uh the impressive team lead in the crochet inc and then also the anusha iyer both cto and uh co-founder and yeah kosher inc the please welcome on the stage about alex and anusha thank you great thanks daniel uh welcome everyone thank you for coming uh it's good to be here in person and thanks to those of us who are also online uh wanted to talk today a little bit about kind of our approach for uh cloud agnostic design and you know really we i just wanted to convey like we're really excited to talk about this because we applied some of these things at our organization really and it's i think i'm not exaggerating when it's changed the way we do business you know it's just a kind of a new way of looking at things um a little bit more about us so yeah as daniel said i'm alex meyer i'm the infrastructure lead at corsa i've been with coursera since 2018 uh discovered kubernetes a few years before that in 2017 actually and i came here from you know places where we really were all in on a certain cloud provider and it kind of got ourselves locked in um so we experienced the pain of that and that cloud provider effectively had pricing power because we were locked in absolutely yeah i'm anusha iyer i'm the cto and one of the co-founders of corsa um introduced to kubernetes through alex in fact and uh you know just fell in love with the whole concept of infrastructure as code i think it really elevates the idea of infrastructure as a first class citizen in the whole software engineering development deployment process and so we've really embraced it head on right into integrating into code reviews and the whole kind of dev pipeline and it's fantastic and excited to tell you more about it today yes so we're going to structure our talk today sort of as a case study of what we've done we'll set the stage early about our app just to kind of give some background and kind of mo
