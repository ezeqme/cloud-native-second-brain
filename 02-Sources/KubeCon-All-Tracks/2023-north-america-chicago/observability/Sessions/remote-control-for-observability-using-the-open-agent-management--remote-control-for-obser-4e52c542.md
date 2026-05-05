---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Observability"
themes: ["AI ML", "Observability"]
speakers: ["Jacob Aronoff", "Lightstep from ServiceNow", "Andy Keller", "observIQ"]
sched_url: https://kccncna2023.sched.com/event/1R2sr/remote-control-for-observability-using-the-open-agent-management-protocol-jacob-aronoff-lightstep-from-servicenow-andy-keller-observiq
youtube_search_url: https://www.youtube.com/results?search_query=Remote+Control+for+Observability+Using+the+Open+Agent+Management+Protocol+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Remote Control for Observability Using the Open Agent Management Protocol - Jacob Aronoff, Lightstep from ServiceNow & Andy Keller, observIQ

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Observability]]
- Temas: [[AI ML]], [[Observability]]
- País/cidade: United States / Chicago
- Speakers: Jacob Aronoff, Lightstep from ServiceNow, Andy Keller, observIQ
- Schedule: https://kccncna2023.sched.com/event/1R2sr/remote-control-for-observability-using-the-open-agent-management-protocol-jacob-aronoff-lightstep-from-servicenow-andy-keller-observiq
- Busca YouTube: https://www.youtube.com/results?search_query=Remote+Control+for+Observability+Using+the+Open+Agent+Management+Protocol+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Remote Control for Observability Using the Open Agent Management Protocol.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2sr/remote-control-for-observability-using-the-open-agent-management-protocol-jacob-aronoff-lightstep-from-servicenow-andy-keller-observiq
- YouTube search: https://www.youtube.com/results?search_query=Remote+Control+for+Observability+Using+the+Open+Agent+Management+Protocol+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=t550FzDi054
- YouTube title: Remote Control for Observability Using the Open Agent Management Prot... Jacob Aronoff & Andy Keller
- Match score: 0.937
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/remote-control-for-observability-using-the-open-agent-management-proto/t550FzDi054.txt
- Transcript chars: 34391
- Keywords: server, configuration, agents, status, config, collector, protocol, remote, message, management, messages, capabilities, bridge, logs, allows, operator, otel, metrics

### Resumo baseado na transcript

hi I'm Andy Keller I'm the principal engineer at observe IQ and a maintainer on the opamp go project within open tretry and I'm Jacob arof from service now I'm a maintainer for the open Telemetry operator project where my focus is on making the otel experience in kubernetes as simple as possible let's say you just bought one of these fancy new electric cars this one is perfect for a quick trip to the beach you get all your stuff together your friends towels everything you need and as

### Excerpt da transcript

hi I'm Andy Keller I'm the principal engineer at observe IQ and a maintainer on the opamp go project within open tretry and I'm Jacob arof from service now I'm a maintainer for the open Telemetry operator project where my focus is on making the otel experience in kubernetes as simple as possible let's say you just bought one of these fancy new electric cars this one is perfect for a quick trip to the beach you get all your stuff together your friends towels everything you need and as you get in your car it says to me to the nearest dealer update my software you'd be pretty upset pretty angry but it's okay you know we have the ability to do remote software updates now so no problem you update your car and you're on the road so you get closer and closer to the beach until your car starts to break down again once again it says Tell me to the nearest dealer I don't know what to do and now you're extra upset but what if the car could just tell you what's wrong and walk you through what to do or maybe it could even fix itself it would be so much better or maybe next time you should just ride your bicycle to the beach it really sucks when cars break down but they keep breaking down ideally the instruments on your car's dashboard will have some info sometimes you'll need to open the hood and take a look yourself it would be pretty awful if the access to both of those key functions to your car's operation weren't available to you software also breaks all the time and we can't always look inside this necessitated the creation of agents that tell us about about the health of our software through dashboards and instruments back before the cloud this would mean you would SSH into an instance and run something like top or tail uh to see how things are doing then the cloud came along and changed it all logs and metrics were the primary ways of understanding your data and for the most part the collection and sending of that was done by an agent an agent in the observability realm is something that looks at how your code is running and reports it somewhere and oh boy are there a lot of Agents they're all configured slightly different and do slightly different things one way of deploying an agent is in its anonomous agent mode this is close to how most agents have been deployed in the past essentially for every application you run you also run an agent that receives your Telemetry processes it and exports it to your Telemetry back end one issue with the agent mode is that i
