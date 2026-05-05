---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Security"
themes: ["AI ML", "Security"]
speakers: ["Yoshiyuki Tabata", "Hitachi", "Ltd."]
sched_url: https://kccncna2025.sched.com/event/27FbM/securing-ai-agent-infrastructure-authnauthz-patterns-for-mcp-and-a2a-yoshiyuki-tabata-hitachi-ltd
youtube_search_url: https://www.youtube.com/results?search_query=Securing+AI+Agent+Infrastructure%3A+AuthN%2FAuthZ+Patterns+for+MCP+and+A2A+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Securing AI Agent Infrastructure: AuthN/AuthZ Patterns for MCP and A2A - Yoshiyuki Tabata, Hitachi, Ltd.

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]]
- País/cidade: United States / Atlanta
- Speakers: Yoshiyuki Tabata, Hitachi, Ltd.
- Schedule: https://kccncna2025.sched.com/event/27FbM/securing-ai-agent-infrastructure-authnauthz-patterns-for-mcp-and-a2a-yoshiyuki-tabata-hitachi-ltd
- Busca YouTube: https://www.youtube.com/results?search_query=Securing+AI+Agent+Infrastructure%3A+AuthN%2FAuthZ+Patterns+for+MCP+and+A2A+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Securing AI Agent Infrastructure: AuthN/AuthZ Patterns for MCP and A2A.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FbM/securing-ai-agent-infrastructure-authnauthz-patterns-for-mcp-and-a2a-yoshiyuki-tabata-hitachi-ltd
- YouTube search: https://www.youtube.com/results?search_query=Securing+AI+Agent+Infrastructure%3A+AuthN%2FAuthZ+Patterns+for+MCP+and+A2A+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=S6qF0N5D1tM
- YouTube title: Securing AI Agent Infrastructure: AuthN/AuthZ Patterns for MCP and A2A - Yoshiyuki Tabata
- Match score: 0.97
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/securing-ai-agent-infrastructure-authn-authz-patterns-for-mcp-and-a2a/S6qF0N5D1tM.txt
- Transcript chars: 20184
- Keywords: authorization, access, request, authentication, server, security, external, pattern, client, workload, internal, exchange, metadata, policy, response, method, patterns, principles

### Resumo baseado na transcript

Today I'd like to talk about securing AI agent infrastructure authentication and authorization patterns for MCP and A2A. In this session I'll share practical authentication and authorization patterns to secure agent infra infrastructure with a focus on MCP and A2A. As a tech lead for CSF tag security and compliance, I contribute to best practices, white papers and proposal reviews and facilitated meetings in the APAC region. However, if A2A use uses weaker credentials such as API keys, it can become the weakest link in the security chain. To maintain a consistent and strong security posture, it's important to align A2A with the same level of assurance as O 2.1 just like MCP. It introduces two security patterns basic and advanced to address different security needs.

### Excerpt da transcript

Hello everyone. Uh thank you for attending this session. I'm Yoshik Tabata from Joso. Today I'd like to talk about securing AI agent infrastructure authentication and authorization patterns for MCP and A2A. In this session I'll share practical authentication and authorization patterns to secure agent infra infrastructure with a focus on MCP and A2A. We'll grant the discussion in the CNC am paper which is expected expected to be published near future and then map these principles to real world implementations using keyroke and spire. By the end of this session you will have a practical blueprint for moving from concept to implementation. So this is today's agenda. First, I'll explain what MCP and ADA are and why they emerged. Next, I'll introduce the CSF IME paper principles and discuss why they matter for agents. Then, I'll present uh concrete authentication authorization patterns for MCP and ATA. Finally, I'll provide a demo showing these ideas in action using keyro. Uh first of all, let me introduce myself.

Uh my name is Yoshik Tavat and I'm a senior consultant at Hitachi. I specialize in securing API and identity for enterprise and clouded platforms with over 10 years of experience designing secure API ecosystems and identity solutions. As a tech lead for CSF tag security and compliance, I contribute to best practices, white papers and proposal reviews and facilitated meetings in the APAC region. I'm also an active open source contributor especially to Kikro as a language maintainer and a feature developer [snorts] and in addition I organize community events such as Kikok on Japan speak at conferences like cubic and write books and articles on IM and Kiko. So let's get started. Uh we'll start with what MCP and A2A are. Uh before AI agent uh LLM could only suggest steps and users had to manually exe execute each action themselves. This limited both uh speed and consistency. AI agents changed this by acting on the user's behalf, automating tasks and human supervision. As the responsibilities of AI agents increased, they needed to communicate with a wide variety of protocols such as SQL, CRIS, REST APIs and many others.

This diversity made integration complicated and often inconsistent. To address this, uh, MCP and ATA were introduced to bring standardization. By adopting these standard protoc protocols, we can reduce the need for custom adapters and make inter operability much easier and more reliable. So first uh what is MCP? MCP is a protocol that sta
