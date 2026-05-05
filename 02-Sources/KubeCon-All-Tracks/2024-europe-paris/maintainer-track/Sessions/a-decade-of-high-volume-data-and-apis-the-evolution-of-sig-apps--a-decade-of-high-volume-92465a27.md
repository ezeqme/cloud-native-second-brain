---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Maintainer Track"
themes: ["AI ML", "Storage Data", "Community Governance"]
speakers: ["Maciej Szulik", "Red Hat", "Janet Kuo", "Google"]
sched_url: https://kccnceu2024.sched.com/event/1YhfK/a-decade-of-high-volume-data-and-apis-the-evolution-of-sig-apps-maciej-szulik-red-hat-janet-kuo-google
youtube_search_url: https://www.youtube.com/results?search_query=A+Decade+of+High-Volume+Data+and+APIs%3A+The+Evolution+of+SIG-Apps+CNCF+KubeCon+2024
slides: []
status: parsed
---

# A Decade of High-Volume Data and APIs: The Evolution of SIG-Apps - Maciej Szulik, Red Hat & Janet Kuo, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Storage Data]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: Maciej Szulik, Red Hat, Janet Kuo, Google
- Schedule: https://kccnceu2024.sched.com/event/1YhfK/a-decade-of-high-volume-data-and-apis-the-evolution-of-sig-apps-maciej-szulik-red-hat-janet-kuo-google
- Busca YouTube: https://www.youtube.com/results?search_query=A+Decade+of+High-Volume+Data+and+APIs%3A+The+Evolution+of+SIG-Apps+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre A Decade of High-Volume Data and APIs: The Evolution of SIG-Apps.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YhfK/a-decade-of-high-volume-data-and-apis-the-evolution-of-sig-apps-maciej-szulik-red-hat-janet-kuo-google
- YouTube search: https://www.youtube.com/results?search_query=A+Decade+of+High-Volume+Data+and+APIs%3A+The+Evolution+of+SIG-Apps+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=bE8XpaJwq-Q
- YouTube title: A Decade of High-Volume Data and APIs: The Evolution of SIG-Apps - Maciej Szulik & Janet Kuo
- Match score: 0.92
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/a-decade-of-high-volume-data-and-apis-the-evolution-of-sig-apps/bE8XpaJwq-Q.txt
- Transcript chars: 23985
- Keywords: controller, workloads, changes, controllers, around, actually, functionality, replica, initial, talking, groups, working, change, started, primarily, version, replication, rewrite

### Resumo baseado na transcript

welcome everyone it's about time we start talking so here we go I guess that's the best option to start this um so Jet and myself will be talking you about the past decade of Sig UPS Janet has been contributing to uh to Sig UPS primarily in the workload space uh since 2015 um and she's been co-chair for Sig ups for almost the same time uh my name is ma uh aside from being an active contributor in the in the batch primarily but also helping with the

### Excerpt da transcript

welcome everyone it's about time we start talking so here we go I guess that's the best option to start this um so Jet and myself will be talking you about the past decade of Sig UPS Janet has been contributing to uh to Sig UPS primarily in the workload space uh since 2015 um and she's been co-chair for Sig ups for almost the same time uh my name is ma uh aside from being an active contributor in the in the batch primarily but also helping with the workloads API I'm also helping with the cube cutle and as of last fall I'm also one of the kubernetes steering committee members and my first contribution dates all the way back to December of 2014 uh there are links to those contributions of ours uh if you're curious about what they were uh the last person that is in charge of sigs is Ken who wasn't able to be with us Ken is actually uh contributing to workloads primarily similarly to Janet his first contribution was a significant refactoring of the stat full set controllers back in um so the Sig apps if you look at the space that we are covering we are actually covering three major API groups within the kubernetes uh ecosystem those three API groups are batched so if you think about jobs Crown jobs um the biggest API Group that we own is around the app so all sorts of uh stateful and stateless uh controllers replica uh replica uh controllers or Damon sets which span all the nodes in your in your running cluster and and lastly the smallest group that is actually uh one of the most important which ensures that whatever disruptions that are happening in your clusters are not affecting your applications um ha functionality so what the early days look like because like the title said we want to go through the past decade of of the kubernetes project with an um with a special focus on what the special interest groups apps was doing over the past 10 years even before uh six were uh initiated so the first officially available taged version of kubernetes was in September of 2014 that was version 0.2 and it was released with a V1 beta API there was no API groups at the time time only single group everyone using were were using just that it was beta one um and the several few resources and that's literally all the resources that the kubernetes cluster had at the time there's literally just pots replication controller uh if you don't know what a replication controller is you can think that it's almost identical to replica Set uh we renamed it later on but both replication
