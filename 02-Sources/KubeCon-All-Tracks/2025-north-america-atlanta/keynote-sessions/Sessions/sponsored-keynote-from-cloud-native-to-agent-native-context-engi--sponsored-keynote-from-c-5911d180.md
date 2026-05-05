---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Keynote Sessions"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Idit Levine", "Founder", "CEO", "Solo.io", "Keith Babo", "Chief Product Officer", "Solo.io"]
sched_url: https://kccncna2025.sched.com/event/27dCV/sponsored-keynote-from-cloud-native-to-agent-native-context-engineering-for-kubernetes-idit-levine-founder-ceo-soloio-keith-babo-chief-product-officer-soloio
youtube_search_url: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+From+Cloud-Native+to+Agent-Native%3A+Context+Engineering+for+Kubernetes+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Sponsored Keynote: From Cloud-Native to Agent-Native: Context Engineering for Kubernetes - Idit Levine, Founder & CEO, Solo.io & Keith Babo, Chief Product Officer, Solo.io

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Idit Levine, Founder, CEO, Solo.io, Keith Babo, Chief Product Officer, Solo.io
- Schedule: https://kccncna2025.sched.com/event/27dCV/sponsored-keynote-from-cloud-native-to-agent-native-context-engineering-for-kubernetes-idit-levine-founder-ceo-soloio-keith-babo-chief-product-officer-soloio
- Busca YouTube: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+From+Cloud-Native+to+Agent-Native%3A+Context+Engineering+for+Kubernetes+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Sponsored Keynote: From Cloud-Native to Agent-Native: Context Engineering for Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27dCV/sponsored-keynote-from-cloud-native-to-agent-native-context-engineering-for-kubernetes-idit-levine-founder-ceo-soloio-keith-babo-chief-product-officer-soloio
- YouTube search: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+From+Cloud-Native+to+Agent-Native%3A+Context+Engineering+for+Kubernetes+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=FxMLmsCavjc
- YouTube title: Sponsored Keynote: From Cloud-Native to Agent-Native: Context Engineering for... I. Levine & K. Babo
- Match score: 0.973
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/sponsored-keynote-from-cloud-native-to-agent-native-context-engineerin/FxMLmsCavjc.txt
- Transcript chars: 4640
- Keywords: agentic, agents, platform, context, registry, production, support, consumption, talking, header, needed, inside, connectivity, gateway, contextaware, engineering, observability, critical

### Resumo baseado na transcript

All right, looking across the industry, there's a clear pattern of agentic AI pilots just never making it to production. The problem is they lack the operational expertise around security, observability, and governance to support those agents when they're in production. Building this uh this data plan for the ground app make it really really useful not only for functionality but also for performance. Today agent gateway has a jaw-dropping performance in terms of throughput and resource consumption. Kubernetes itself needs to be extended to become a contextaware runtime to support that. K agent extends Kubernetes to turn tools and agents into first class workloads on the platform where I can secure observe and get endtoend observability for those agents and tools regardless of the agentic framework or in the environment that I'm running in.

### Excerpt da transcript

All right, looking across the industry, there's a clear pattern of agentic AI pilots just never making it to production. Now, AI teams know how to write agents. That's not the problem. The problem is they lack the operational expertise around security, observability, and governance to support those agents when they're in production. It's critical that as platform teams, we meet and partner with these AI teams to deliver production agentic infrastructure on Kubernetes. So this is why we the platform engineering team need to bring right now all those framework and those MCP2 to Kubernetes but there is some gap. So let's look at the first gap networking when we talking about networking usually we talking about request and request consists from header and a body. In the header you find all the instruction for where and how to run the route and in the body you'll find the context itself. Until today we will never needed to look at the body. All we did is adder manipulation. But now with AI we have to look at the body.

We don't have a choice as important information is there. So let me give you some example. LLM consumption. Let's say that I want to route based on rate limiting based on token right what we need to do we need to go to the body take the agent context sending to basically um tokenize that and then rate paste this so again I need to go to the body to take that context if we're talking about MCP it's even more clear right because MCP it says JSON RPC over HTTP so the HTTP P part is the header but the JSON RPC all the data and we need all the tools is actually in the body. There are great proxies out there and all of them implement perfectly all the way to the layer 7. We as Envy company when we wanted to add the functionality of AI to um the proxy we of course try to put it inside Android and with LM consumption it was tough. We needed to tweak Android a little bit but somehow we make it work. But when MCP came it was a clear thing that we will not be able to do this without rearchitect envoy and that will take years.

So we made a decision. We basically made a decision to build a from the ground up a data plan in Rust that will give us everything we need for AI. So we started and of course first we needed to implement all the first layer seven because AI workloads still need retry and timeouts. Then we added what we're calling the L the eight layer the context layer to focus on LLM consumption inference agent and MCP connectivity. We add support fo
