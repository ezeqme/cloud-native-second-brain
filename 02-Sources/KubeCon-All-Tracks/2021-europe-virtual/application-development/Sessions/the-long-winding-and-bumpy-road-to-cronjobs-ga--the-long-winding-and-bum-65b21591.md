---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Application + Development"
themes: ["Application + Development"]
speakers: ["Maciej Szulik", "Red Hat", "Alay Patel", "Red Hat"]
sched_url: https://kccnceu2021.sched.com/event/iE1V/the-long-winding-and-bumpy-road-to-cronjobs-ga-maciej-szulik-red-hat-alay-patel-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=The+Long%2C+Winding+and+Bumpy+Road+to+CronJob%E2%80%99s+GA+CNCF+KubeCon+2021
slides: []
status: parsed
---

# The Long, Winding and Bumpy Road to CronJob’s GA - Maciej Szulik, Red Hat & Alay Patel, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Application + Development]]
- Temas: [[Application + Development]]
- País/cidade: Virtual / Virtual
- Speakers: Maciej Szulik, Red Hat, Alay Patel, Red Hat
- Schedule: https://kccnceu2021.sched.com/event/iE1V/the-long-winding-and-bumpy-road-to-cronjobs-ga-maciej-szulik-red-hat-alay-patel-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=The+Long%2C+Winding+and+Bumpy+Road+to+CronJob%E2%80%99s+GA+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre The Long, Winding and Bumpy Road to CronJob’s GA.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE1V/the-long-winding-and-bumpy-road-to-cronjobs-ga-maciej-szulik-red-hat-alay-patel-red-hat
- YouTube search: https://www.youtube.com/results?search_query=The+Long%2C+Winding+and+Bumpy+Road+to+CronJob%E2%80%99s+GA+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=o5h6s3A9bXY
- YouTube title: The Long, Winding and Bumpy Road to CronJob’s GA - Maciej Szulik, Red Hat & Alay Patel, Red Hat
- Match score: 0.772
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/the-long-winding-and-bumpy-road-to-cronjobs-ga/o5h6s3A9bXY.txt
- Transcript chars: 21740
- Keywords: controller, schedule, actually, scheduled, function, server, informer, update, resource, controllers, handler, process, create, informers, handlers, handle, current, scheduling

### Resumo baseado na transcript

hi i am oleg madel and my name is mate and today i'm going to take you to a long winding and bumpy road to crown jobs ga the idea of cron jobs wasn't entirely new in the distributed world identical mechanism was already available in google's internal cluster management system borg which divided workloads in two basic categories long-running services and bad jobs for the remaining part of this presentation we'll focus on the latter it wasn't long after kubernetes was officially announced by google in mid 2014 that back then writing controllers was completely different from what it is today the controller was periodically pulling all scheduler jobs and triggering the ones that were supposed to run this way seemed the simplest and most obvious to solve the problem at the time after challenge was that for a few releases we actually supported both the old scheduler jobs and a new cronjobs name which wasn't an easy thing to do eventually in 1.8 we've decided to promote cron jobs to beta without too much changes in the api or the controller that was back in 2017 until 2020 hit us from many angles for us the biggest impact was the proposal to remove all the so-called perma beta apis from kubernetes in the near future the community gathered around special interest group devoted to running application or sigaps in short debated the problem for every api where we've been impacted...

### Excerpt da transcript

hi i am oleg madel and my name is mate and today i'm going to take you to a long winding and bumpy road to crown jobs ga the idea of cron jobs wasn't entirely new in the distributed world identical mechanism was already available in google's internal cluster management system borg which divided workloads in two basic categories long-running services and bad jobs for the remaining part of this presentation we'll focus on the latter it wasn't long after kubernetes was officially announced by google in mid 2014 that this functionality will be needed in this project as well my first exposure to this topic was in the spring of 2015 when a bunch of us here at red hat along with our customers and small community that has gathered around kubernetes before its 1.0 release later that year we started tinkering with this problem and writing down our thoughts first in openshift repository in may june of that year eventually reaching consensus i've opened a proposal back in august 2015. only after we moved our proposal to kubernetes repository more people including the authors of the borg paper started looking at it the proposal was sliced and diced into many directions eventually we've agreed to split the topic into two first the original proposal morphed from describing distributed cron functionality to a primitive which allows running a task to completion today this is simply known as a job resource this way our focus slightly shifted and we dived into implementing jobs which were part of 1.1 release of kubernetes it's important to mention the fact that back then kubernetes did not have api groups like it has today so adding a new resource was challenging to say the least on top of that jobs and cron jobs were very often trade blazers in the areas of api groups and versions finally after shipping jobs in january of 2016 i was able to finally focus on the initial ask what i haven't mentioned before is that back then cron jobs were actually called schedule at jobs naming his heart isn't it honestly i can't remember the reasoning behind the name but i'm pretty sure it is still there in those proposals and discussions at that moment in time we've all had a pretty good understanding of the topic as well as the primitives and mechanism to build scheduled jobs so as soon as the proposal was merged we jumped into the implementation even though we initially targeted 1.3 release we had to delay the functionality until 1.4 due to many challenges i've mentioned before this way i
