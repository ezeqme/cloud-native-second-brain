---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Tutorials"
themes: ["Observability", "Community Governance"]
speakers: ["Hannah Troisi", "Vihang Mehta", "Michelle Nguyen", "New Relic", "Clemens Kolbitsch", "VMware"]
sched_url: https://kccnceu2023.sched.com/event/1HyeB/tutorial-building-an-open-source-observability-stack-hannah-troisi-vihang-mehta-michelle-nguyen-new-relic-clemens-kolbitsch-vmware
youtube_search_url: https://www.youtube.com/results?search_query=Tutorial%3A+Building+an+Open+Source+Observability+Stack+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Tutorial: Building an Open Source Observability Stack - Hannah Troisi, Vihang Mehta & Michelle Nguyen, New Relic; Clemens Kolbitsch, VMware

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Tutorials]]
- Temas: [[Observability]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Hannah Troisi, Vihang Mehta, Michelle Nguyen, New Relic, Clemens Kolbitsch, VMware
- Schedule: https://kccnceu2023.sched.com/event/1HyeB/tutorial-building-an-open-source-observability-stack-hannah-troisi-vihang-mehta-michelle-nguyen-new-relic-clemens-kolbitsch-vmware
- Busca YouTube: https://www.youtube.com/results?search_query=Tutorial%3A+Building+an+Open+Source+Observability+Stack+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Tutorial: Building an Open Source Observability Stack.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyeB/tutorial-building-an-open-source-observability-stack-hannah-troisi-vihang-mehta-michelle-nguyen-new-relic-clemens-kolbitsch-vmware
- YouTube search: https://www.youtube.com/results?search_query=Tutorial%3A+Building+an+Open+Source+Observability+Stack+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=0XwwCp1NQyQ
- YouTube title: Tutorial: Building an Open Source Observability Stack - Troisi, Mehta & Nguyen, Kolbitsch
- Match score: 0.856
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/tutorial-building-an-open-source-observability-stack/0XwwCp1NQyQ.txt
- Transcript chars: 55007
- Keywords: metrics, actually, application, logs, prometheus, cluster, observability, fluent, information, traces, request, essentially, collect, trace, allows, storage, source, interesting

### Resumo baseado na transcript

thank you for coming to our tutorial building an open source observability stack um let's just introduce ourselves here so my name is Hannah and I work at New Relic and primarily on contributing to pixie hi everyone I'm Michelle and I also work at New Relic I'm one of the maintainers of Pixie and later I'll be walking you through the demo that we have at the end hi I'm vihang I also work at neuralik and I'm one of the maintainers for pixie hi everyone and I'm Clements

### Excerpt da transcript

thank you for coming to our tutorial building an open source observability stack um let's just introduce ourselves here so my name is Hannah and I work at New Relic and primarily on contributing to pixie hi everyone I'm Michelle and I also work at New Relic I'm one of the maintainers of Pixie and later I'll be walking you through the demo that we have at the end hi I'm vihang I also work at neuralik and I'm one of the maintainers for pixie hi everyone and I'm Clements I am not one of the maintainers or developers of Pixie I'm actually from VMware and I represent more of one of you guys so essentially I am a user of Pixie and I will walk you through not only open Telemetry but also how do we use these tools in one of the projects that VMware to show you kind of how to get observability and what to do with that data all right let's get started so it's it's super interesting right there was a cncf study last year where they were asking what observability tools do you use and what are the challenges that you see and more than half of the people said they are actually struggling with just a sheer volume of different tools that different teams are using so this is a problem that we need to address right observability has many many different ways many different things you can collect many ways that you can collect them stored and visualize it and so on and so part of what we want to do today is really walk you guys through what is observability how do you do this how do you instruct instrument your code to detect all these things how do you store them how do you visualize them just how they get observable observability in your cluster and Kate's is actually very specific in terms of separability because there's just so many open source tools and we want to guide you down a path of understanding what are the most common tools out there which ones might be specifically interesting for your environment and how do you actually use them so we first want to walk through very high level what are the tools and then in the second section Michelle is going to walk you through all right Hands-On how do I get this done so one other thing that is super interesting is you know because there are so many open source Technologies you can ask yourself okay how do I avoid being locked into one because it is very very tricky if you make wrong assumptions wrong decisions early in your project to say what if I later want to change something does that mean I have to rebuild my entire o
