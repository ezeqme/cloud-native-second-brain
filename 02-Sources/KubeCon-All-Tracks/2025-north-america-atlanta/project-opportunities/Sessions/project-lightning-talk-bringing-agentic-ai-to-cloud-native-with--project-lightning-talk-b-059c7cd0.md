---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Project Opportunities"
themes: ["AI ML", "Community Governance"]
speakers: ["Eitan Yarmush", "Lead Maintainer"]
sched_url: https://kccncna2025.sched.com/event/28yEd/project-lightning-talk-bringing-agentic-ai-to-cloud-native-with-kagent-eitan-yarmush-lead-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Bringing+Agentic+AI+To+Cloud+Native+With+Kagent+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Bringing Agentic AI To Cloud Native With Kagent - Eitan Yarmush, Lead Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Eitan Yarmush, Lead Maintainer
- Schedule: https://kccncna2025.sched.com/event/28yEd/project-lightning-talk-bringing-agentic-ai-to-cloud-native-with-kagent-eitan-yarmush-lead-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Bringing+Agentic+AI+To+Cloud+Native+With+Kagent+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Bringing Agentic AI To Cloud Native With Kagent.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/28yEd/project-lightning-talk-bringing-agentic-ai-to-cloud-native-with-kagent-eitan-yarmush-lead-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Bringing+Agentic+AI+To+Cloud+Native+With+Kagent+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=oXBr9UAOG2M
- YouTube title: Project Lightning Talk: Bringing Agentic AI To Cloud Native With Kagent - Eitan Yarmush
- Match score: 0.989
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-bringing-agentic-ai-to-cloud-native-with-kagent/oXBr9UAOG2M.txt
- Transcript chars: 3448
- Keywords: actually, prompt, define, welcome, message, llm, interact, framework, agents, thought, anyone, lightning, bringing, agentic, native, kagent, rethinking, source

### Resumo baseado na transcript

I'm an architect at solo.io and a maintainer on K agent as well as agent gateway. So I think the way that I want to spend my time here actually is less so about K agent and more so about really what an agent is right and why we created this uh project. Now this when we looked at this at solo we thought wait this is just declarative right why can't we run this in kubernetes like we run every other workload uh that we talk about so when we thought about that we came up with So, K agent really is the system that puts all this together in a way that both is easy to run on Kubernetes and can be used generally, but is also super easy to understand for anyone who is inculcated or involved in the uh in the Kubernetes ecosystem like all of us are and have a lovehate relationship with YAML, but at the end of the day, we all know how we feel.

### Excerpt da transcript

Welcome to uh I'm welcome to the talk about K agent. Um I call it rethinking the open source agent stack. Uh my name is Eton Yarmish. I'm an architect at solo.io and a maintainer on K agent as well as agent gateway. So you know obviously we don't have a lot of time. So I think the way that I want to spend my time here actually is less so about K agent and more so about really what an agent is right and why we created this uh project. I don't think we're at the point yet where we can say here's the update. You know why am I here? Why did we create K agent? Well, what really is an agent? An agent is made up of three things. A system prompt, an LM, and tools. That's it really. When it comes down to it, that's all you need to remember. So, what is the the core loop of the agent, right? I'm Bob. I always like to use Bob in my presentations. Bob sends a message. The system prompt gets appended. Uh gets sent to the LM. The LLM decides if it needs to call tools, right? That goes back. If it needs to call more tools, it keeps going.

Otherwise, it goes back to the user. Awesome. So, what are these tools, right? These are the way that that the agent actually takes actions, whether it's GitHub, Docker, Slack, some sort of object storage. Now, many of you have probably heard of MCP. MCP is sort of like the USB of tool connection, right? It's how all these different systems know how to interact with various tools. So all basically every project now has an MCP server to be able to interact with it and this is going to evolve in the future but that's how it works right now. Um so what are the so when I think about an agent I really think about a seven layer cake. Uh it's not actually seven layers but I like seven layer cake. So at the top level you have your framework right your framework is orchestrating your agents and your agents are using tools. Now this when we looked at this at solo we thought wait this is just declarative right why can't we run this in kubernetes like we run every other workload uh that we talk about so when we thought about that we came up with an API we said great all right well we have an agent and the agent connects to tools so can I just define my agent in YAML again I just all I said was that it's a system message and an LLM and tools so I have a model config I define it there.

I have a system prompt. I define it there. And I have tools that I've defined there. That's it. And now all of a sudden I have an agent done. Amazing. So, K agent re
