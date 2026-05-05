---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Yong Tang", "Ivanti"]
sched_url: https://kccncna2022.sched.com/event/182Mu/coredns-intro-and-deep-dive-yong-tang-ivanti
youtube_search_url: https://www.youtube.com/results?search_query=CoreDNS+Intro+And+Deep+Dive+CNCF+KubeCon+2022
slides: []
status: parsed
---

# CoreDNS Intro And Deep Dive - Yong Tang, Ivanti

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Detroit
- Speakers: Yong Tang, Ivanti
- Schedule: https://kccncna2022.sched.com/event/182Mu/coredns-intro-and-deep-dive-yong-tang-ivanti
- Busca YouTube: https://www.youtube.com/results?search_query=CoreDNS+Intro+And+Deep+Dive+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre CoreDNS Intro And Deep Dive.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Mu/coredns-intro-and-deep-dive-yong-tang-ivanti
- YouTube search: https://www.youtube.com/results?search_query=CoreDNS+Intro+And+Deep+Dive+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6TkrrZLxQeo
- YouTube title: CoreDNS Intro And Deep Dive - Yong Tang, Ivanti
- Match score: 0.841
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/coredns-intro-and-deep-dive/6TkrrZLxQeo.txt
- Transcript chars: 27571
- Keywords: coding, plugin, another, server, information, question, several, google, request, actually, discuss, company, public, simple, write, itself, easily, default

### Resumo baseado na transcript

okay first of all thanks for coming to this session uh my name is y I'm a Mena of coding as project uh joining me today is John bammer he is a Committee Member of C project joh maybe you read your hand okay okay okay yeah in today's session we are going to discuss several things first we are going to discuss about uh some Community update of codings uh as well as ing progress in some of feature that have been recently added and then I'm going to demo so the core file will be just the demo it will the plugin uh the plugin has to be compiled you know it has to be compiled a part of the coding as repo so into fet coding repo you add a demo to you will see a coding as binary on your local uh on your local directory you can just invoke coding as and that's all okay that's uh uh demo plugin and again like I said the the source code is available if you're interested in start writing your own plugins and you I highly encourage you to to use this demo plugin as a starting point and also if you check the whole repo the whole repo only consist of like eight lines of goola so it should be simple out so the source of the data can be backed by Google Cloud it can be backed by um uh Route 53 it can be backed by a file it can be backed by a post database it can be backed by uh kubernetes API

### Excerpt da transcript

okay first of all thanks for coming to this session uh my name is y I'm a Mena of coding as project uh joining me today is John bammer he is a Committee Member of C project joh maybe you read your hand okay okay okay yeah in today's session we are going to discuss several things first we are going to discuss about uh some Community update of codings uh as well as ing progress in some of feature that have been recently added and then I'm going to introduce a little bit of survey disc Discovery and the coding s and show example of how coding s can be used to consolidate different information from different Cloud windows and finally I'm going to uh do a deep dive of codings and go through a demo plugin that allows uh anyone uh with the knowledge of Golan to write a codinance plugin in potentially like less than 100 lines of Goan code uh and also by the way uh if you have any question you can certainly raise your hand uh I'll try to answer as much as possible and also JN is here maybe JN can answer some more question as well okay let's uh let's first uh discuss about codings so as many of you know codings is a s SF project uh it's a flexible D server WR in go uh unlike other DS server DS project CS has a focus on service Discovery it it is a a plugin base which means it can be easily extended in other word if you have any features uh you're looking for you can either uh look for external Plugin or internal Plugin or if you know how to write uh if you know how to write in goong then you can write the plugin for by yourself uh one of the most important uh uh features of coding as is coding as is a default DS server in covid-19 so I guess anyone using coding anyone using kubernetes probably will use the as coding as by default in addition to to be served as a default DS server Cod DS also support different protocols it support DNS D DNS over TOS DNS over JPC it also support additional protocol like DS over ATP uh in addition to in addition to those different protocols another thing cing as Excel way is the consolidation of different Cloud uh Cloud related DS information for example with cods you can syncer with the aw ra hisory you can syncer with a DNS or you can syn up with Google Cloud DNS that give you plenty of flexibility and allows you to consolidate in case you're doing a multic cloud deployment and finally uh coding as was started by uh MC dben uh several years ago um as of recently MC dben decided to uh stepping down uh from the project lead position so
