---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Tutorials"
themes: ["Networking", "GitOps Delivery"]
speakers: ["Nina Polshakova", "Lawrence Gadban", "Solo.io"]
sched_url: https://kccncna2024.sched.com/event/1i7ok/tutorial-no-mess-rollouts-with-gateway-api-leveraging-gateway-api-and-argo-rollouts-for-progressive-delivery-nina-polshakova-lawrence-gadban-soloio
youtube_search_url: https://www.youtube.com/results?search_query=Tutorial%3A+No+Mess+Rollouts+with+Gateway+API%3A+Leveraging+Gateway+API+and+Argo+Rollouts+for+Progressive+Delivery+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Tutorial: No Mess Rollouts with Gateway API: Leveraging Gateway API and Argo Rollouts for Progressive Delivery - Nina Polshakova & Lawrence Gadban, Solo.io

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Tutorials]]
- Temas: [[Networking]], [[GitOps Delivery]]
- País/cidade: United States / Salt Lake City
- Speakers: Nina Polshakova, Lawrence Gadban, Solo.io
- Schedule: https://kccncna2024.sched.com/event/1i7ok/tutorial-no-mess-rollouts-with-gateway-api-leveraging-gateway-api-and-argo-rollouts-for-progressive-delivery-nina-polshakova-lawrence-gadban-soloio
- Busca YouTube: https://www.youtube.com/results?search_query=Tutorial%3A+No+Mess+Rollouts+with+Gateway+API%3A+Leveraging+Gateway+API+and+Argo+Rollouts+for+Progressive+Delivery+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Tutorial: No Mess Rollouts with Gateway API: Leveraging Gateway API and Argo Rollouts for Progressive Delivery.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7ok/tutorial-no-mess-rollouts-with-gateway-api-leveraging-gateway-api-and-argo-rollouts-for-progressive-delivery-nina-polshakova-lawrence-gadban-soloio
- YouTube search: https://www.youtube.com/results?search_query=Tutorial%3A+No+Mess+Rollouts+with+Gateway+API%3A+Leveraging+Gateway+API+and+Argo+Rollouts+for+Progressive+Delivery+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=H67jKACtPHs
- YouTube title: Tutorial: No Mess Rollouts with Gateway API: Leveraging Gateway API and... N. Polshakova, L. Gadban
- Match score: 0.854
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/tutorial-no-mess-rollouts-with-gateway-api-leveraging-gateway-api-and/H67jKACtPHs.txt
- Transcript chars: 79354
- Keywords: canary, gateway, actually, argo, deployment, stable, rollouts, version, traffic, replica, revision, command, header, virtual, create, analysis, change, control

### Resumo baseado na transcript

go cool um well so we're going to do a workshop on no mess rollouts with API Gateway so if you're interested in Argo and uh API Gateway you're in the right place um I'm Nina uh I work at solo as a software engineer um we do primarily ISO and uh our API uh gate Envoy based API Gateway so I've been on kind of both teams so very familiar with ISO and Envoy um I'm Lawrence yeah I'm Lawrence uh I also work at solo working on the

### Excerpt da transcript

go cool um well so we're going to do a workshop on no mess rollouts with API Gateway so if you're interested in Argo and uh API Gateway you're in the right place um I'm Nina uh I work at solo as a software engineer um we do primarily ISO and uh our API uh gate Envoy based API Gateway so I've been on kind of both teams so very familiar with ISO and Envoy um I'm Lawrence yeah I'm Lawrence uh I also work at solo working on the same things as well cool well so before uh like we get into more slides um our lab takes a while to boot up um and this is like a Hands-On Workshop so if you don't have a laptop find a buddy uh scan the QR code or go to the link um and this is all an instruct so you don't have to run anything locally it's you know in the like the internet should be okay since it's running on on their VMS um so yeah so scan the QR code it'll take a couple minutes maybe to boot up um so if you start now we'll like have the slide throughout the presentation so if you come late and need to scan like it'll return um but if you want to do that now and get started that would be great um and uh the next thing we're going to do is actually take um some warm-up questions so um the first warm-up question is uh if you are using a Gateway controller which one are you using are you using you know AWS um ISO um what other yeah psyllium Kong glue uh Envoy Gateway um so yeah but yeah if you slide if or if you swipe yeah there you go so some answers for AWS some answers for esto more ISO engine X we'll actually see that maybe later Envoy Gateway we'll also see that cool Ambassador very good more AWS AWS yeah a good number of engine X too which is good this one of our examples uh might might use that so all right give people another couple seconds to to keep typing it's a pretty good yeah I think might be the winner yeah all right well um all good answers um we have another question too so if you finish typing I'll move on to the second question um so my second question is how familiar are you with Progressive delivery techniques so this is mostly to help us like you know speed the like you know understand what speed to go at um in the early sections because we're going to assume um like no knowledge um of arar roll outs to begin with and kind of introduce it gradually um so yeah so somewhat familiar good to hear great so it seems like people have some familiarity with like what Argo is or what Progressive delivery is um so with that I'm going to put up the the lab link a
