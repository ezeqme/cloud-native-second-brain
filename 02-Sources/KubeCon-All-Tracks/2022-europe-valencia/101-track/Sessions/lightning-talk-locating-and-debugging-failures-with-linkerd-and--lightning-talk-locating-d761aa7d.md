---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "101 Track"
themes: ["AI ML"]
speakers: ["Alejandro Pedraza", "Buoyant", "Edidiong Asikpo", "Ambassador Labs"]
sched_url: https://kccnceu2022.sched.com/event/ytwm/lightning-talk-locating-and-debugging-failures-with-linkerd-and-telepresence-alejandro-pedraza-buoyant-edidiong-asikpo-ambassador-labs
youtube_search_url: https://www.youtube.com/results?search_query=Lightning+Talk%3A+Locating+and+Debugging+Failures+with+Linkerd+and+Telepresence+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Lightning Talk: Locating and Debugging Failures with Linkerd and Telepresence - Alejandro Pedraza, Buoyant & Edidiong Asikpo, Ambassador Labs

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[101 Track]]
- Temas: [[AI ML]]
- País/cidade: Spain / Valencia
- Speakers: Alejandro Pedraza, Buoyant, Edidiong Asikpo, Ambassador Labs
- Schedule: https://kccnceu2022.sched.com/event/ytwm/lightning-talk-locating-and-debugging-failures-with-linkerd-and-telepresence-alejandro-pedraza-buoyant-edidiong-asikpo-ambassador-labs
- Busca YouTube: https://www.youtube.com/results?search_query=Lightning+Talk%3A+Locating+and+Debugging+Failures+with+Linkerd+and+Telepresence+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Lightning Talk: Locating and Debugging Failures with Linkerd and Telepresence.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytwm/lightning-talk-locating-and-debugging-failures-with-linkerd-and-telepresence-alejandro-pedraza-buoyant-edidiong-asikpo-ambassador-labs
- YouTube search: https://www.youtube.com/results?search_query=Lightning+Talk%3A+Locating+and+Debugging+Failures+with+Linkerd+and+Telepresence+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=E13a_CDGRV4
- YouTube title: Lightning Talk: Locating and Debugging Failures with Linkerd... Alejandro Pedraza & Edidiong Asikpo
- Match score: 0.873
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/lightning-talk-locating-and-debugging-failures-with-linkerd-and-telepr/E13a_CDGRV4.txt
- Transcript chars: 4014
- Keywords: cluster, problems, voting, linker, emojis, working, header, debugging, telepresence, namespace, components, traffic, operating, success, scroll, requests, actually, permission

### Resumo baseado na transcript

when i started valencia my name is alejandro pederasa i'm a software engineer at buoyant my name is [Music] linker d is the fastest and lightest service mesh [Music] okay this app allows you to vote for emojis you have a leaderboard to see what are the favorite emojis among your users we have deployed these in a cluster whose spots are listed here we have under the emoji photo namespace the components that make up our app we also have the link rd control plane installed and link rdv's

### Excerpt da transcript

when i started valencia my name is alejandro pederasa i'm a software engineer at buoyant my name is [Music] linker d is the fastest and lightest service mesh [Music] okay this app allows you to vote for emojis you have a leaderboard to see what are the favorite emojis among your users we have deployed these in a cluster whose spots are listed here we have under the emoji photo namespace the components that make up our app we also have the link rd control plane installed and link rdv's which is an extension that gives you extra visibility and that we will use in a moment and we have ambassadors traffic manager pod which coordinates all the intercepts happening in this cluster now let's say users have been complaining about problems in our app even though it's working fine for us as we just saw so in order to take a deeper look into what's going on we're going to launch linker tv's dashboard and the first thing we see is that the emoji photo namespace is not operating at a 100 success rate so let's click there we see the components that make up our app emoji and vote bot are operating at a 100 success rate but visibly voting and web are the ones having trouble so let's click on web in this diagram we see how traffic flows into and out of web we see that web depends on a service called voting and apparently that's the service responsible for the errors so let's click there if we scroll down a little bit we see all the requests coming into this pod everything is looking fine so far but we start seeing problems vote donut is failing consistently so most likely that is the source of all our problems up until now we have used linker d to identify the location of the problems in our cluster now i'm going to hand it over to edition to show us how we can use telepresence to debug and actually fix the problem to the voting service in our permission as you can see in the command we've also passed a special http header named keycon and what that is you need to do is basically signifying that only requests with this header should be passed to the voting service on our local mission and any request without this headline to deposit service on our nexus so now that we have that working and the reason why we're doing that is to ensure that while we're testing and debugging it doesn't affect other developers on our team so with that i'm going to quickly start the emojigo service on our permission and then i'm going to pass the header which is default and coupon you don't hav
