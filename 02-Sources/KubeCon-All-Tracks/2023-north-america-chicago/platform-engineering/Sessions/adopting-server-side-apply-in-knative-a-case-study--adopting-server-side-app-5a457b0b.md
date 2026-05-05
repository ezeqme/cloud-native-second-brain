---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Platform Engineering"
themes: ["Platform Engineering"]
speakers: ["Dave Protasowski", "VMware"]
sched_url: https://kccncna2023.sched.com/event/1R2ny/adopting-server-side-apply-in-knative-a-case-study-dave-protasowski-vmware
youtube_search_url: https://www.youtube.com/results?search_query=Adopting+Server+Side+Apply+in+Knative+-+a+Case+Study+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Adopting Server Side Apply in Knative - a Case Study - Dave Protasowski, VMware

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]]
- País/cidade: United States / Chicago
- Speakers: Dave Protasowski, VMware
- Schedule: https://kccncna2023.sched.com/event/1R2ny/adopting-server-side-apply-in-knative-a-case-study-dave-protasowski-vmware
- Busca YouTube: https://www.youtube.com/results?search_query=Adopting+Server+Side+Apply+in+Knative+-+a+Case+Study+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Adopting Server Side Apply in Knative - a Case Study.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2ny/adopting-server-side-apply-in-knative-a-case-study-dave-protasowski-vmware
- YouTube search: https://www.youtube.com/results?search_query=Adopting+Server+Side+Apply+in+Knative+-+a+Case+Study+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=1rlTPjQ9dco
- YouTube title: Adopting Server Side Apply in Knative - a Case Study - Dave Protasowski, VMware
- Match score: 0.886
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/adopting-server-side-apply-in-knative-a-case-study/1rlTPjQ9dco.txt
- Transcript chars: 30357
- Keywords: fields, server, resource, update, actually, controller, client, controllers, create, tooling, config, resources, conflict, multiple, native, essentially, trying, autoscaler

### Resumo baseado na transcript

okay cool um apologies for my raspy voice it's the Midwest air I guess um coming from Toronto uh welcome to my talk it um it's about adopting service side apply my name is Dave perosi jump in uh I am first intro I'm a Staff engineer at VMware potentially soon to be broadcom to be determined who mystery um uh I work on can of open source project I'm the serving lead and I'm also on the technical oversight committee there um some links I still use the Twitter

### Excerpt da transcript

okay cool um apologies for my raspy voice it's the Midwest air I guess um coming from Toronto uh welcome to my talk it um it's about adopting service side apply my name is Dave perosi jump in uh I am first intro I'm a Staff engineer at VMware potentially soon to be broadcom to be determined who mystery um uh I work on can of open source project I'm the serving lead and I'm also on the technical oversight committee there um some links I still use the Twitter Bluebird because I like it I haven't updated my Twitter W in two years so still works uh for the agenda today I'm going to cover um kind of like what's the problem with client side apply kind of go into a quick overview of server side apply kind of talk about K native and then how service side apply impacts how I view we can adopt it in k and sort of like the status of um my work there and the learnings that I have so client side update is essentially kind of like what most controllers are doing also when you do cou cuto apply is the default application of applying resources to a server so kind of like an example of a problem is let's say we have a config map on the API server and we have two people trying to update it so the first application from um let's say that's me uh will update it and then subsequently another person doing an update uh potentially can cause a conflict if they have like resource version set and so forth like that so what does the other person have to do they might need to redo the application but if they don't properly update that um config map with what's from the server then event eventually you lose and you have some data loss um and kind of what that means is you'll get conflicts or most controllers encounter conflicts so if you see 409s when you do a lot of controller updates that means then you got to do refetch and retry the request if you're ref fetching and retrying is very dumb for whatever reason um you have potential data loss and a lot of um issues that I see or we we've encountered is you get infinite churn where we have controllers fighting each other once try to update one the other one's trying to update the other there's loss so they see something's not there they keep going forever and then you'll see your observe Generation Um Spike up quite a bit um so surface side apply um going to steal the definition from the docks it's actually pretty useful uh mult or so first the fields of a single object I kind of just want to cover this a little bit in detail so what
