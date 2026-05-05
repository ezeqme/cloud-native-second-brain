---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Networking"
themes: ["AI ML", "Observability", "Networking", "Storage Data"]
speakers: ["Laurent Bernaille", "Elijah Andrews", "Datadog"]
sched_url: https://kccnceu2022.sched.com/event/ytrw/logs-told-us-it-was-dns-it-felt-like-dns-it-had-to-be-dns-it-wasnt-dns-laurent-bernaille-elijah-andrews-datadog
youtube_search_url: https://www.youtube.com/results?search_query=Logs+Told+Us+It+Was+DNS%2C+It+Felt+Like+DNS%2C+It+Had+To+Be+DNS%2C+It+Wasn%E2%80%99t+DNS+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Logs Told Us It Was DNS, It Felt Like DNS, It Had To Be DNS, It Wasn’t DNS - Laurent Bernaille & Elijah Andrews, Datadog

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Networking]]
- Temas: [[AI ML]], [[Observability]], [[Networking]], [[Storage Data]]
- País/cidade: Spain / Valencia
- Speakers: Laurent Bernaille, Elijah Andrews, Datadog
- Schedule: https://kccnceu2022.sched.com/event/ytrw/logs-told-us-it-was-dns-it-felt-like-dns-it-had-to-be-dns-it-wasnt-dns-laurent-bernaille-elijah-andrews-datadog
- Busca YouTube: https://www.youtube.com/results?search_query=Logs+Told+Us+It+Was+DNS%2C+It+Felt+Like+DNS%2C+It+Had+To+Be+DNS%2C+It+Wasn%E2%80%99t+DNS+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Logs Told Us It Was DNS, It Felt Like DNS, It Had To Be DNS, It Wasn’t DNS.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytrw/logs-told-us-it-was-dns-it-felt-like-dns-it-had-to-be-dns-it-wasnt-dns-laurent-bernaille-elijah-andrews-datadog
- YouTube search: https://www.youtube.com/results?search_query=Logs+Told+Us+It+Was+DNS%2C+It+Felt+Like+DNS%2C+It+Had+To+Be+DNS%2C+It+Wasn%E2%80%99t+DNS+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=NunyPkN0n3c
- YouTube title: Logs Told Us It Was DNS, It Felt Like DNS, It Had To Be DNS, I... Laurent Bernaille & Elijah Andrews
- Match score: 0.895
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/logs-told-us-it-was-dns-it-felt-like-dns-it-had-to-be-dns-it-wasnt-dns/NunyPkN0n3c.txt
- Transcript chars: 36730
- Keywords: actually, metric, seeing, connection, happening, interface, seconds, traffic, contract, instance, packet, errors, requests, connections, network, second, thousands, looked

### Resumo baseado na transcript

welcome to uh kubecon welcome to our talk it's so great to be here in person and to see uh everyone here uh it's been a tough two years and it's really great that we're doing these things again so today we're going to talk about the time that it wasn't dns everything seemed to tell us that it was dns the logs it felt like dns it had to be dns and it wasn't so first off we're here representing datadog uh this is a talk about datadog's infrastructure removing it from dns and then after this external dns runs in a sync loop there's a fun balancing act here between like how frequently you want updates and how big you want your batches to be because you can hit problems with rate limits

### Excerpt da transcript

welcome to uh kubecon welcome to our talk it's so great to be here in person and to see uh everyone here uh it's been a tough two years and it's really great that we're doing these things again so today we're going to talk about the time that it wasn't dns everything seemed to tell us that it was dns the logs it felt like dns it had to be dns and it wasn't so first off we're here representing datadog uh this is a talk about datadog's infrastructure not about uh the product that we have but just in case you're not familiar we're an observability platform we monitor all the things we have a sweet booth in the exhibition hall and you should go check it out we're doing a raffle for a nintendo switch uh this afternoon so you should go get your badge scanned and see what we have to offer anyway uh the numbers that i want to focus on for this talk are the way that we run kubernetes and we're really big on that technology we run it at a big scale just to give you an idea we have some figures on the right-hand column here so we run thousands of tens of thousands of nodes and hundreds of thousands of pods we have dozens of kubernetes clusters with anywhere from hundreds to thousands of nodes so we're running this at a very large scale we run on uh all the major cloud providers and we're growing very quickly but before we dive too deep into the talk i'll let you know who we are so i'm elijah andrews i'm a software engineer at datadog i work on our service discovery and network infrastructure and i'm lauren birnai i'm staff engineer i work in an infrastructure also and i like to focus and dive into weird and fun networking issues as the one we're going to discuss today all right so let's talk about how this all started so we have a we have a service called the metric service at datadog and the people who operate the service notice that when they did a rollout and a rolling restart they would see a large spike in errors so you can see there are two lines here on that top graph the one of the lines the the purple one corresponds to the server and you can see here that during a rolling restart which is what was happening here uh there's a huge spike in errors the red line there is showing the this from the client's perspective the client actually retried so it didn't show up as an error rate in the client however our latency went up by a lot because the clients had to retry and this was degrading performance in our application so as we always do when we have problems wit
