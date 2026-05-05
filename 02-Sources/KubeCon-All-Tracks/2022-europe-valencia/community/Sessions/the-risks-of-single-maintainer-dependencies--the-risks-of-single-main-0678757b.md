---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Community"
themes: ["AI ML", "Community Governance"]
speakers: ["John McBride", "VMware"]
sched_url: https://kccnceu2022.sched.com/event/ytlk/the-risks-of-single-maintainer-dependencies-john-mcbride-vmware
youtube_search_url: https://www.youtube.com/results?search_query=The+Risks+of+Single+Maintainer+Dependencies+CNCF+KubeCon+2022
slides: []
status: parsed
---

# The Risks of Single Maintainer Dependencies - John McBride, VMware

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Community]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Spain / Valencia
- Speakers: John McBride, VMware
- Schedule: https://kccnceu2022.sched.com/event/ytlk/the-risks-of-single-maintainer-dependencies-john-mcbride-vmware
- Busca YouTube: https://www.youtube.com/results?search_query=The+Risks+of+Single+Maintainer+Dependencies+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre The Risks of Single Maintainer Dependencies.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytlk/the-risks-of-single-maintainer-dependencies-john-mcbride-vmware
- YouTube search: https://www.youtube.com/results?search_query=The+Risks+of+Single+Maintainer+Dependencies+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=YBsDnXXW_d8
- YouTube title: The Risks of Single Maintainer Dependencies - John McBride, VMware
- Match score: 0.891
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/the-risks-of-single-maintainer-dependencies/YBsDnXXW_d8.txt
- Transcript chars: 37562
- Keywords: projects, maintainer, important, person, within, around, maintainers, getting, contributor, question, communities, packages, dependencies, incentives, software, actually, single, without

### Resumo baseado na transcript

uh this is the risks of single maintainer dependencies um bear with me still dealing with the jet lag but in this talk we are going to chat about the lottery factor contributor communities and the secure software supply chain so one of the things i always ask myself whenever i show up to one of these talks is okay well who the heck are you and yes i promise it is relevant for this talk uh so my name is john mcbride i'm a senior software engineer at vmware

### Excerpt da transcript

uh this is the risks of single maintainer dependencies um bear with me still dealing with the jet lag but in this talk we are going to chat about the lottery factor contributor communities and the secure software supply chain so one of the things i always ask myself whenever i show up to one of these talks is okay well who the heck are you and yes i promise it is relevant for this talk uh so my name is john mcbride i'm a senior software engineer at vmware and i work on our open source kubernetes platform which is tanzania community edition along with a bunch of ancillary open source projects around that kubernetes kind and one of those projects is spf 13 cobra now if you don't know what cobra is is it's a cli bootstrapping library for go that gives you a bunch of really nice apis for creating commands and a really modern cli application tons of stuff uses it all over the cncf all over kubernetes so just some quick statistics here on cobra itself it has over 26 000 stars on github it has over 900 commits and again it is a key dependency in the cncf kubernetes ecosystem uh just to touch on a few projects that use it kubernetes itself cube cuddle helm tanzu at vmware docker cd istio lingard the github cli i mean it's everywhere if it was written and go it probably uses cobra let's uh touch on a brief history of cobra here cobra's first commit was in 2013 and it came out of sort of that same group at google that was doing that was doing core go so it sat right at home within kubernetes and with cube cuddle and a lot of the stuff that came out of kubernetes in the early days of go for example here is the default cube cuddle command that returns us a cobra command it really is the entry point for your actual implementation of your actual features and all the stuff you're actually trying to do cobra wraps around all of that stuff let's fast forward to today and this is the 1.4.0 release that i cut in march and something interesting to i guess realize about where we're at today with cobra is that i more or less maintain cobra by myself now before i go any further let's define what maintaining means here i have admin privileges on the repository i can merge code so merge pull requests i can triage issues close issues and i can cut releases they're sending those packages sending those apis into kubernetes into vmware into red hat into google all over and again before i continue here a huge shout out to the cobra community it's actually gotten much better recently so
