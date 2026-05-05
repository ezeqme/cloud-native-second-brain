---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Community Governance"]
speakers: ["Mike Dame", "Jan Chaloupka", "Red Hat"]
sched_url: https://kccnceu2021.sched.com/event/iE7P/sig-scheduling-intro-and-deep-dive-mike-dame-jan-chaloupka-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=SIG+Scheduling+Intro+and+Deep+Dive+CNCF+KubeCon+2021
slides: []
status: parsed
---

# SIG Scheduling Intro and Deep Dive - Mike Dame & Jan Chaloupka, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Virtual / Virtual
- Speakers: Mike Dame, Jan Chaloupka, Red Hat
- Schedule: https://kccnceu2021.sched.com/event/iE7P/sig-scheduling-intro-and-deep-dive-mike-dame-jan-chaloupka-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=SIG+Scheduling+Intro+and+Deep+Dive+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre SIG Scheduling Intro and Deep Dive.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE7P/sig-scheduling-intro-and-deep-dive-mike-dame-jan-chaloupka-red-hat
- YouTube search: https://www.youtube.com/results?search_query=SIG+Scheduling+Intro+and+Deep+Dive+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=R2CpmLfHUYk
- YouTube title: SIG-Scheduling Intro and Deep Dive - Wei Huang, IBM
- Match score: 0.909
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/sig-scheduling-intro-and-deep-dive/R2CpmLfHUYk.txt
- Transcript chars: 22649
- Keywords: scheduling, schedule, scheduler, default, plugin, plugins, cluster, another, resource, called, filter, option, already, second, scheduled, config, weight, percentage

### Resumo baseado na transcript

hi everyone welcome to today's session uh today i'm going to to give you a deep dive on the sixth scheduling my name is i work for ibm and i'm also the current co-chair of the sikh scheduling so today's agenda contains three parts first i will give you a brief introduction on schedule and then we'll share with you some best practice tips and so that you can make the most of your schedule and the third part is i will give you some update on the latest development to get the best of all performance we used to have the pr2 wanted to set this to the uh cpu cost number but it seems doesn't work properly so we revert up here so if you want to [Music] customize this and want to

### Excerpt da transcript

hi everyone welcome to today's session uh today i'm going to to give you a deep dive on the sixth scheduling my name is i work for ibm and i'm also the current co-chair of the sikh scheduling so today's agenda contains three parts first i will give you a brief introduction on schedule and then we'll share with you some best practice tips and so that you can make the most of your schedule and the third part is i will give you some update on the latest development progress so firstly what does scheduler exactly do so in short-term limit terms scheduler just does one thing which is to put the path to the nose so that means it doesn't evolve into the path creation it also doesn't evolve into the spin of the underlying containers you just find a node for the pending path and technical terms so basically scheduler will watch the pending path which which means the path doesn't have the spectrum name set and then it will look into the part explicit scheduling constraint like cpu memory requests another affinity et cetera and also taking some predefined implicit scheduling preference into consideration and look at the cluster resource usage and make the decision to place the path to the optimal node so this is what scheduler does and inside scheduler there are basically several components the first one we call the caching so to make the most optimal decision schedule has to maintain a cache to have a sort of choose view of the whole cluster like how many nails are there how many tiles are there and how many pv pvcs etc etc so scheduler we run internal fuel scheduling formulas to watch for the api objects so that we can maintain the internal cache properly and the second part is called queuing so if a pi is coming to the queue we schedule it with reasonable order so internally we have a priority queue and if there's no note fit for the path we also have some back off mechanism to ensure the lower priority part has a chance to be scheduled and also the path can have a fair chance to be re-popped up and be retried and also next uh our main scheduling goal routine and binding routine which is a serious processes to do the core scheduling flow so the core scheduling flow looks like this so firstly we will pick apart from the scratching queue and we will go through a series what we call extension point here so for each extension point we have a series of plugins and we will go through those plugins either sequentially or in parallel depends on what phase it is it will fi
