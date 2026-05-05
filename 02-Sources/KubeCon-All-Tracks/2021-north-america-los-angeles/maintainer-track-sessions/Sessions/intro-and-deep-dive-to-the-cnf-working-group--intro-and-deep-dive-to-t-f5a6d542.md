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
speakers: ["Ian Wells", "Cisco", "Jeffrey Saelens", "Charter Communications", "Taylor Carpenter", "Vulk Coop"]
sched_url: https://kccncna2021.sched.com/event/lV9e/intro-and-deep-dive-to-the-cnf-working-group-ian-wells-cisco-jeffrey-saelens-charter-communications-taylor-carpenter-vulk-coop
youtube_search_url: https://www.youtube.com/results?search_query=Intro+and+Deep+Dive+to+the+CNF+Working+Group+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Intro and Deep Dive to the CNF Working Group - Ian Wells, Cisco; Jeffrey Saelens, Charter Communications; Taylor Carpenter, Vulk Coop

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Los Angeles
- Speakers: Ian Wells, Cisco, Jeffrey Saelens, Charter Communications, Taylor Carpenter, Vulk Coop
- Schedule: https://kccncna2021.sched.com/event/lV9e/intro-and-deep-dive-to-the-cnf-working-group-ian-wells-cisco-jeffrey-saelens-charter-communications-taylor-carpenter-vulk-coop
- Busca YouTube: https://www.youtube.com/results?search_query=Intro+and+Deep+Dive+to+the+CNF+Working+Group+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Intro and Deep Dive to the CNF Working Group.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV9e/intro-and-deep-dive-to-the-cnf-working-group-ian-wells-cisco-jeffrey-saelens-charter-communications-taylor-carpenter-vulk-coop
- YouTube search: https://www.youtube.com/results?search_query=Intro+and+Deep+Dive+to+the+CNF+Working+Group+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=I2FVayIn_yo
- YouTube title: Intro and Deep Dive to the CNF Working Group - Ian Wells, Jeffrey Saelens, Taylor Carpenter
- Match score: 0.752
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/intro-and-deep-dive-to-the-cnf-working-group/I2FVayIn_yo.txt
- Transcript chars: 23455
- Keywords: practices, infrastructure, working, trying, actually, network, software, native, applications, itself, finally, interface, developers, specifically, packets, operators, platform, challenges

### Resumo baseado na transcript

hello everybody and welcome to this session which is about the cnf working group um i'll just make some quick introductions there are three of us co-chairs and we're all going to have a little chat with you today my name's ian wells i work for cisco i build cnfs my co-chair there from charter is jeff salence he runs cnfs and taylor carpenter is how many in the community who makes sure that they all work on kubernetes so what we're going to talk about today is why the

### Excerpt da transcript

hello everybody and welcome to this session which is about the cnf working group um i'll just make some quick introductions there are three of us co-chairs and we're all going to have a little chat with you today my name's ian wells i work for cisco i build cnfs my co-chair there from charter is jeff salence he runs cnfs and taylor carpenter is how many in the community who makes sure that they all work on kubernetes so what we're going to talk about today is why the cnf exists how it was started what we're trying to do and how we're trying to make the world a better place for those of us who actually need to run cnfs for a living um so a quick intro to the group itself um uh we were formed um at uh kubecon um about a year ago at this point um it was a collaboration between a bunch of us um service providers telcos need to actually run cnfs as vendors need to make cnfs and again as i say we need to make it so it's possible to create these things they're not that easy to create and consume these things because um you know it's easy to get um into the weeds when you're trying to run complex software um and we're going to do that by publicizing the best practices that we've learned for both the development and the operation um a cnf for those of you aren't quite aware on that is a cloud native network function so we're not just looking for containerized but actually cloud native um that influence or facilitates network functionality so it might be moving individual network packets around or it might be something that supervises or controls or transfers information about where those packets go so we include uh actual things like routers but we also include things like reflectors bgp and you know this crosses the board into other um areas of networking like mobile networks we obviously want to design at least we want to enable design of those cnfs as microservices as well structured applications using the best practices that we already know from the kubernetes world um with immutable infrastructure with declarative apis and of course repeatable deployment um but we also need to deal with the things where cnfs are a little bit different and special so our problems basically amount to the difficulty in making these things work cns are hard to develop and operate and we want to simplify that we want to make it so that developing a cnf is not something that you you spend so long trying to figure out how even that works uh we want to make sure that um you follow the
