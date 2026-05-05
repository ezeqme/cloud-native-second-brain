---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Platform Engineering"
themes: ["AI ML", "Platform Engineering"]
speakers: ["Shivay Lamba", "Couchbase", "Ekansh Gupta", "SigNoz"]
sched_url: https://kccncna2025.sched.com/event/27Fb7/designing-platforms-with-judgment-agentic-flows-with-mcp-shivay-lamba-couchbase-ekansh-gupta-signoz
youtube_search_url: https://www.youtube.com/results?search_query=Designing+Platforms+With+Judgment%3A+Agentic+Flows+With+MCP+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Designing Platforms With Judgment: Agentic Flows With MCP - Shivay Lamba, Couchbase & Ekansh Gupta, SigNoz

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[AI ML]], [[Platform Engineering]]
- País/cidade: United States / Atlanta
- Speakers: Shivay Lamba, Couchbase, Ekansh Gupta, SigNoz
- Schedule: https://kccncna2025.sched.com/event/27Fb7/designing-platforms-with-judgment-agentic-flows-with-mcp-shivay-lamba-couchbase-ekansh-gupta-signoz
- Busca YouTube: https://www.youtube.com/results?search_query=Designing+Platforms+With+Judgment%3A+Agentic+Flows+With+MCP+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Designing Platforms With Judgment: Agentic Flows With MCP.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Fb7/designing-platforms-with-judgment-agentic-flows-with-mcp-shivay-lamba-couchbase-ekansh-gupta-signoz
- YouTube search: https://www.youtube.com/results?search_query=Designing+Platforms+With+Judgment%3A+Agentic+Flows+With+MCP+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=nrNmqxbRzok
- YouTube title: Designing Platforms With Judgment: Agentic Flows With MCP - Shivay Lamba & Ekansh Gupta
- Match score: 0.892
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/designing-platforms-with-judgment-agentic-flows-with-mcp/nrNmqxbRzok.txt
- Transcript chars: 28347
- Keywords: platform, server, context, application, engineering, servers, github, create, basically, understand, entire, docker, platforms, everything, protocol, intervention, argo, logs

### Resumo baseado na transcript

Hi everyone uh I am Ianch I am a software engineer with signos and signnos is a open source open telemetry native observability platform and here with me is shai and >> yeah hi everyone I'm shay I'm a CN ambassador and Dr. We have already discussed about uh like platform engineering with you folks. And uh once that whole application is there in your kubernetes cluster or in your environment you would need some kind of observability. Uh but you can use any of the back ends such as signal prometheus graphana uh which will collect your metrics events logs and traces your general four pillars of observability to figure out if something is going wrong with your application in your environment. So that's where incident management comes in and uh for incident management you need something like pager duty or slack uh alerts or something like that where uh engineer is always on call. So I know the pain points where uh I get a pager duty alert and I need to be active my s SR needs to be active.

### Excerpt da transcript

Hi everyone uh I am Ianch I am a software engineer with signos and signnos is a open source open telemetry native observability platform and here with me is shai and >> yeah hi everyone I'm shay I'm a CN ambassador and Dr. captain and um looking forward to this talk. >> Yeah. So let's get started with the session. We have already discussed about uh like platform engineering with you folks. So uh what we are going to talk about in this session is that we wanted to design platforms with judgment some platforms which are uh proactive in nature and not just reactive and how do we achieve them with MCPS the agentic flows with MCP. So the session title is as written designing platforms with judgment. Let's go with uh what are the traditional platform engineering practices. So uh I I have like a couple of years of experience in platform engineering teams now and uh the things that are in common with all the teams is that human intervention is the most needed in a platform engineering team. So let's just say I want to develop an application and I want to deploy it over uh GitHub like push it over GitHub for something.

So uh we push the code and uh it triggers a CI/CD pipeline. The it can be either GitHub actions, it can be genkins and the deployment goes through Argo CD or some other CD platform that you are using. Apart from that we need some pipelines to build it and run it in production. And uh once that whole application is there in your kubernetes cluster or in your environment you would need some kind of observability. So I would prefer like open telemetry as your default observability standard. Uh but you can use any of the back ends such as signal prometheus graphana uh which will collect your metrics events logs and traces your general four pillars of observability to figure out if something is going wrong with your application in your environment. Apart from that once that is done once that is sorted uh your application might be running fine your application might not be running fine. So that's where incident management comes in and uh for incident management you need something like pager duty or slack uh alerts or something like that where uh engineer is always on call.

So I there have been days where I have been on call for like seven days straight. So I know the pain points where uh I get a pager duty alert and I need to be active my s SR needs to be active. So a a lot of human intervention is always needed. So why is pro platform engineering so cum
