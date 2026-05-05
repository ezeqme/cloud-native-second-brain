---
type: kubecon-session
event: "KubeCon + CloudNativeCon China 2025 - Hong Kong, China"
event_id: kccncchn2025
year: 2025
region: "China"
city: "Hong Kong"
country: "China"
event_date: "2025"
track: "Connectivity"
themes: ["Networking"]
speakers: ["Sayan Mondal", "Harness", "Jintao Zhang", "Kong Inc."]
sched_url: https://kccncchn2025.sched.com/event/1x5ip/guardians-of-the-gateway-keeping-chaos-out-of-your-cloud-highway-sayan-mondal-harness-jintao-zhang-kong-inc
youtube_search_url: https://www.youtube.com/results?search_query=Guardians+of+the+Gateway%3A+Keeping+Chaos+Out+of+Your+Cloud+Highway+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Guardians of the Gateway: Keeping Chaos Out of Your Cloud Highway - Sayan Mondal, Harness & Jintao Zhang, Kong Inc.

## Identificação

- Edição: KubeCon + CloudNativeCon China 2025 - Hong Kong, China
- Trilha oficial: [[Connectivity]]
- Temas: [[Networking]]
- País/cidade: China / Hong Kong
- Speakers: Sayan Mondal, Harness, Jintao Zhang, Kong Inc.
- Schedule: https://kccncchn2025.sched.com/event/1x5ip/guardians-of-the-gateway-keeping-chaos-out-of-your-cloud-highway-sayan-mondal-harness-jintao-zhang-kong-inc
- Busca YouTube: https://www.youtube.com/results?search_query=Guardians+of+the+Gateway%3A+Keeping+Chaos+Out+of+Your+Cloud+Highway+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Guardians of the Gateway: Keeping Chaos Out of Your Cloud Highway.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncchn2025.sched.com/event/1x5ip/guardians-of-the-gateway-keeping-chaos-out-of-your-cloud-highway-sayan-mondal-harness-jintao-zhang-kong-inc
- YouTube search: https://www.youtube.com/results?search_query=Guardians+of+the+Gateway%3A+Keeping+Chaos+Out+of+Your+Cloud+Highway+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6V-2xKUCV7A
- YouTube title: Guardians of the Gateway: Keeping Chaos Out of Your Cloud Highway - Sayan Mondal & Jintao Zhang
- Match score: 0.911
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/guardians-of-the-gateway-keeping-chaos-out-of-your-cloud-highway/6V-2xKUCV7A.txt
- Transcript chars: 14909
- Keywords: operator, gateway, public, application, another, experiments, litmus, engineering, experiment, systems, insomia, product, integration, discuss, called, reliability, basically, partner

### Resumo baseado na transcript

Uh today we are going to discuss uh something which is about gateways, something about chaos. Uh and the title of our talk is guardians of the gateway, keeping chaos out of your cloud highways. The business impact is also massive because 81% of augs reported that just one hour of downtime costs over $300,000 and in the last year alone 50% of those companies experienced an API related security incident. So APIs like I said are the glue of the modern architecture because they are um reliant on like they are basically what's managing u your application across dozens of services. Uh for example we have we built some uh tools for example insomia insomia can we can use insomia for API debug API design and testing. uh and uh for the uh connect the platform uh we can do some uh some task for example API government and API regist and API observability uh yeah we can use a lot of plugins to enhancement the API security and we can uh

### Excerpt da transcript

Hello everyone. Um I hope you're having a great coupon so far. Uh today we are going to discuss uh something which is about gateways, something about chaos. Uh and the title of our talk is guardians of the gateway, keeping chaos out of your cloud highways. Uh we are two speakers. My name is Shy. I'm a senior software engineer to at Harness. Uh I also maintain uh the project called Litmos Chaos which is the chaos engineering opensource framework which we'll see and discuss today. Uh and I'm also an active LFX mentor uh and a chaos engineering practitioner of course and this is my GitHub handle. I'll let Ginta introduce himself. Uh thank you everyone. Uh I'm Ginta work at the call and I'm one of the CNCF ambassador Microsoft MVP and Kubernetes ingress and maintainer. All right. So we will start today with the discussion on APIs and we'll see how it affects reliability. So we know that APIs have become the backbone of our software systems of our modern software systems anyways, right? So they accelerate innovation.

They help us scale faster and they also enable integrations across platforms. So APIs are very crucial not just to for login or to fetch customer details or user data. They are everywhere. So they are very powerful but they're also like a double-edged sword. As you can see they're using so many different outlets in health, work, travel, transportation and so on. Now ideally not every API is visible or even properly managed. Uh there's a there's a thing called shadow APIs which are created uh not not in the centralized uh but are not in the centralized oversight. So they are increasingly common and they introduce a lot of risk and the truth is every API transaction is critical uh whether it's login payment or even user data but they matter because it's not just a function call it's a potential uh point of failure worse is every API is also an attack vector because the surface area is huge uh and they are they basically expose a lot of logic and data that the attackers can exploit and they don't always go through you know your traditional firewalls.

And to make things even more complex, no two APIs are alike. So they're built by different teams using different protocols. You have REST, you have GraphQL, you have gRPC deployed across different stacks, um clouds, regions and so on. This fragmentation specifically uh makes governance and controlling them observability incredibly hard. And we are not even keeping up with this because uh according to Ga
