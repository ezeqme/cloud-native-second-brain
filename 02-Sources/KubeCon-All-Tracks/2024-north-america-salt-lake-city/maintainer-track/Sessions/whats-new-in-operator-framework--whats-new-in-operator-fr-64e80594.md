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
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Bryce Palmer", "Rashmi Gottipati", "Lalatendu Mohanty", "Red Hat", "Attila Meszaros", "Apple"]
sched_url: https://kccncna2024.sched.com/event/1hoxy/whats-new-in-operator-framework-bryce-palmer-rashmi-gottipati-lalatendu-mohanty-red-hat-attila-meszaros-apple
youtube_search_url: https://www.youtube.com/results?search_query=What%27s+New+in+Operator+Framework%3F%21+CNCF+KubeCon+2024
slides: []
status: parsed
---

# What's New in Operator Framework?! - Bryce Palmer, Rashmi Gottipati & Lalatendu Mohanty, Red Hat; Attila Meszaros, Apple

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Bryce Palmer, Rashmi Gottipati, Lalatendu Mohanty, Red Hat, Attila Meszaros, Apple
- Schedule: https://kccncna2024.sched.com/event/1hoxy/whats-new-in-operator-framework-bryce-palmer-rashmi-gottipati-lalatendu-mohanty-red-hat-attila-meszaros-apple
- Busca YouTube: https://www.youtube.com/results?search_query=What%27s+New+in+Operator+Framework%3F%21+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre What's New in Operator Framework?!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1hoxy/whats-new-in-operator-framework-bryce-palmer-rashmi-gottipati-lalatendu-mohanty-red-hat-attila-meszaros-apple
- YouTube search: https://www.youtube.com/results?search_query=What%27s+New+in+Operator+Framework%3F%21+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=XaIXWHKuzzI
- YouTube title: What's New in Operator Framework?
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/whats-new-in-operator-framework/XaIXWHKuzzI.txt
- Transcript chars: 21203
- Keywords: operator, controller, bundle, operators, hybrid, create, version, runtime, hopefully, override, framework, specific, control, little, basically, already, plugins, everything

### Resumo baseado na transcript

what's new in operator framework uh so today we have myself i'm jesus rodriguez principal software engineer at red hat i'm the team lead for the operator sdk team there and with me is jonathan hey uh my name is jonathan burkhahan i'm a open source software contributor for ibm uh maintainer on the sdk uh which is what we're here to talk to you about today so show of hands how many of you have heard of the operator framework wow i'm impressed um what about operator sdk or

### Excerpt da transcript

what's new in operator framework uh so today we have myself i'm jesus rodriguez principal software engineer at red hat i'm the team lead for the operator sdk team there and with me is jonathan hey uh my name is jonathan burkhahan i'm a open source software contributor for ibm uh maintainer on the sdk uh which is what we're here to talk to you about today so show of hands how many of you have heard of the operator framework wow i'm impressed um what about operator sdk or olm okay cube builder controller runtime wow that's great you guys have you surprised me i honestly was expecting not very many hands so this is really happy so what is operator framework it's an open source toolkit to help you create and manage your operators there's two key projects operator sdk which is the cli it's an extensible toolkit that can scaffold out your projects and help you create bundles to integrate with olm olm operator lifecycle manager will help you it helps you get your install manage and upgrade your operators so basically it takes away a lot of the hard work and just kind of lets it run and manage it for you it also has a dependency model as well sdk uses other upstream projects controller tools cube builder and controller runtime as well so what's new we just recently added java's based operator support to the operator sdk so what are java operators they're effectively operators that you write in java simple as that so they we've currently have go and ansible and helm support so now we can actually help you create your operator scaffold it out in native java we were able to do this there is a new plugin java operators plugin which integrates with sdk that does the scaffolding of it and then there is a java operator sdk project that was started by another group that is effectively a controller runtime library like except written in java so it allows us to not have to do a lot of the lower level kubernetes pieces in java and and it makes it easier to develop your operator for the first version of the plug-in we're actually scaffolding out a corkus based operator so using quarkus runtime it'll make it faster and it's and kind of reduces a lot of the code when we actually scaffold it so why did we do the java operators well one of the reasons is there were a bunch of java developers everyone says it's the popular enterprise language so we wanted to kind of target there we have a mantra of meeting the developers of where they are so instead of forcing folks to learn go an
