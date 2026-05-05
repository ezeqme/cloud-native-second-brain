---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Security + Identity + Policy"
themes: ["AI ML", "Security", "Sustainability"]
speakers: ["Chip Zoller", "Nirmata", "Brandt Keller", "Defense Unicorns"]
sched_url: https://kccncna2022.sched.com/event/182Ju/path-to-production-sustainable-compliance-in-strict-environments-chip-zoller-nirmata-brandt-keller-defense-unicorns
youtube_search_url: https://www.youtube.com/results?search_query=Path+To+Production%3A+Sustainable+Compliance+In+Strict+Environments+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Path To Production: Sustainable Compliance In Strict Environments - Chip Zoller, Nirmata & Brandt Keller, Defense Unicorns

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[AI ML]], [[Security]], [[Sustainability]]
- País/cidade: United States / Detroit
- Speakers: Chip Zoller, Nirmata, Brandt Keller, Defense Unicorns
- Schedule: https://kccncna2022.sched.com/event/182Ju/path-to-production-sustainable-compliance-in-strict-environments-chip-zoller-nirmata-brandt-keller-defense-unicorns
- Busca YouTube: https://www.youtube.com/results?search_query=Path+To+Production%3A+Sustainable+Compliance+In+Strict+Environments+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Path To Production: Sustainable Compliance In Strict Environments.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Ju/path-to-production-sustainable-compliance-in-strict-environments-chip-zoller-nirmata-brandt-keller-defense-unicorns
- YouTube search: https://www.youtube.com/results?search_query=Path+To+Production%3A+Sustainable+Compliance+In+Strict+Environments+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=1tivKIprMsw
- YouTube title: Path To Production: Sustainable Compliance In Strict Environments - Chip Zoller & Brandt Keller
- Match score: 0.911
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/path-to-production-sustainable-compliance-in-strict-environments/1tivKIprMsw.txt
- Transcript chars: 32736
- Keywords: compliance, environment, environments, control, policy, compliant, controls, satisfied, cluster, source, validate, policies, regulated, change, ability, information, definition, looking

### Resumo baseado na transcript

all right welcome everyone I'm your track host for this session uh my name is pushker we have chip and brand who are going to talk to us about path to production sustainable compliance in strict environments chip BR take it away hello everyone thanks for being here this is our session path to production sustainable compliance and strict environments my name is chipz I am a technical product manager at derata and also a CNO maintainer hey everyone my name is Brank Keller um I'm a software engineer at

### Excerpt da transcript

all right welcome everyone I'm your track host for this session uh my name is pushker we have chip and brand who are going to talk to us about path to production sustainable compliance in strict environments chip BR take it away hello everyone thanks for being here this is our session path to production sustainable compliance and strict environments my name is chipz I am a technical product manager at derata and also a CNO maintainer hey everyone my name is Brank Keller um I'm a software engineer at defense unicorns and kind of our talk today is to kind of walk through some design patterns around you know how can we create sustainable compliance in these um regulated environments and really regulated is called out here because it's more of an extreme case but as we look to commercial environments we as we look to just general our Dev environments we want to be thinking about okay who does this impact um why does it impact should I be looking at specific things about my data Etc um so we're going to kind of walk through a couple things um stick with us to the end we're going to have a demo to kind of walk through some automation that'll be a little bit more exciting um but we definitely have to set the stage right um a regulated environment um what is it uh typically if you think about that your your healthare financial government uh Etc um some of these environments that we're building kubernetes uh on various Cloud providers they need to meet compliance with a certain set of Standards um I.E your your nists 853s Etc um and we've been doing it for a while now it's it you know it's working for us but how can we start to push into you know what's what's the best path forward how can we automate compliance as a part of how we're delivering software to these environments um and so there's there's definitely a lot of things that go into that um the like Optimal scenario that we're talking about here with regulated environments is we want to know um absolutely to the most granular layer like what is being introduced into our environment um and I think that's very important I think we're if we're thinking about kubernetes in particular we're definitely at the cross-section of get Ops with declarative configuration um it's going to be pretty explicit about hey this is I'm changing I'm making the change in somewhere that requires approvals and reviews in order for it to then be introduced into the environment um and on top of that or maybe as a layer below that we
