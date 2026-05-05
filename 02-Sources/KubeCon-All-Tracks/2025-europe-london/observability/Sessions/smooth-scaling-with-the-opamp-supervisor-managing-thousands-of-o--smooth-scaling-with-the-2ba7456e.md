---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Observability"
themes: ["Observability", "SRE Reliability"]
speakers: ["Evan Bradley", "Dynatrace", "Andy Keller", "observIQ"]
sched_url: https://kccnceu2025.sched.com/event/1txID/smooth-scaling-with-the-opamp-supervisor-managing-thousands-of-opentelemetry-collectors-evan-bradley-dynatrace-andy-keller-observiq
youtube_search_url: https://www.youtube.com/results?search_query=Smooth+Scaling+With+the+OpAMP+Supervisor%3A+Managing+Thousands+of+OpenTelemetry+Collectors+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Smooth Scaling With the OpAMP Supervisor: Managing Thousands of OpenTelemetry Collectors - Evan Bradley, Dynatrace & Andy Keller, observIQ

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Observability]]
- Temas: [[Observability]], [[SRE Reliability]]
- País/cidade: United Kingdom / London
- Speakers: Evan Bradley, Dynatrace, Andy Keller, observIQ
- Schedule: https://kccnceu2025.sched.com/event/1txID/smooth-scaling-with-the-opamp-supervisor-managing-thousands-of-opentelemetry-collectors-evan-bradley-dynatrace-andy-keller-observiq
- Busca YouTube: https://www.youtube.com/results?search_query=Smooth+Scaling+With+the+OpAMP+Supervisor%3A+Managing+Thousands+of+OpenTelemetry+Collectors+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Smooth Scaling With the OpAMP Supervisor: Managing Thousands of OpenTelemetry Collectors.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txID/smooth-scaling-with-the-opamp-supervisor-managing-thousands-of-opentelemetry-collectors-evan-bradley-dynatrace-andy-keller-observiq
- YouTube search: https://www.youtube.com/results?search_query=Smooth+Scaling+With+the+OpAMP+Supervisor%3A+Managing+Thousands+of+OpenTelemetry+Collectors+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=g8rtqqNTL9Q
- YouTube title: Smooth Scaling With the OpAMP Supervisor: Managing Thousands of OpenTe... Evan Bradley & Andy Keller
- Match score: 0.931
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/smooth-scaling-with-the-opamp-supervisor-managing-thousands-of-opentel/g8rtqqNTL9Q.txt
- Transcript chars: 25240
- Keywords: collector, server, supervisor, configuration, agents, custom, messages, running, config, components, management, remote, looking, basically, implementation, extension, message, capability

### Resumo baseado na transcript

Uh I'm an approver of the opamp spec and a maintainer of the go implementation and work on the architecture and implementation of bindplane a telemetry pipeline management platform. Um I'm an approver on the go uh op amp implementation and uh I help maintain both the supervisor and the op amp extension in the collector. While the project lives within the open telemetry GitHub organization, opamp design is designed to be agent agnostic. If you'd like to learn more, I gave a talk about opamp at CubeCon North America in 2023 with Jacob Aronov. Uh and the supervisor will gather logs through std out and make sure that those end up uh in your telemetry back end as well. So, you can learn more about this by looking at the readme for opamp custom messages.

### Excerpt da transcript

Welcome to smooth scaling with the op amp supervisor. I'm Andy Keller. I'm the principal engineer at Bineplane. Uh I'm an approver of the opamp spec and a maintainer of the go implementation and work on the architecture and implementation of bindplane a telemetry pipeline management platform. And I'm Evan Bradley. I'm an engineer at Datrace and a collector maintainer. Um I'm an approver on the go uh op amp implementation and uh I help maintain both the supervisor and the op amp extension in the collector. So we're going to start with an intro in introduction and update of the opamp protocol. Then we'll look at implementation of opamp and the open telemetry collector and the role of the opamp supervisor. And we'll demonstrate opamp working in an agent management server and finally talk about what's coming next for opamp and the supervisor. So how many are familiar with opamp? Show hands. Familiar with the supervisor. Anybody using op amp? All right. So, opamp stands for open agent management protocol. It's a network protocol for remote management of large fleets of observability agents.

The specification is available within the open telemetry github organization and a go implementation is also available. It contains a client and server SDKs uh and provides some example implementations. Opamp is used to connect agents to an agent management server. The server can coordinate telemetry agents, reporting on their status, sending them configuration, upgrading their packages, and it provides a command and control interface to a large fleet of agents. The protocol supports both HTTP and websockets. In the case of HTTP, it pulls for updates from the server periodically and websockets use a persistent connection to the server and messages can be pushed to the agent directly. App defins agent to server and server to agent. As you can guess by the names, they contain data sent in each direction. By looking at the different components of the agent to server message, we can answer basic questions like what agents do I have? Are they healthy? What are they doing? What can they do? The message sent from the server to the agent describes what the server can do.

And it can also instruct the agent to use a particular configuration or provide packages for modifying the agent and can also send commands to the agent. While the project lives within the open telemetry GitHub organization, opamp design is designed to be agent agnostic. We hope that other agents in the future wil
