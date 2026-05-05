---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Platform Engineering"
themes: ["AI ML", "Platform Engineering", "SRE Reliability"]
speakers: ["Alvaro Saurin", "Jose M Navarro", "Adobe"]
sched_url: https://kccnceu2026.sched.com/event/2CVyx/enterprise-scale-migrations-using-agentic-workflows-with-human-in-the-loop-alvaro-saurin-jose-m-navarro-adobe
youtube_search_url: https://www.youtube.com/results?search_query=Enterprise-Scale+Migrations+Using+Agentic+Workflows+with+Human-in-the-loop+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Enterprise-Scale Migrations Using Agentic Workflows with Human-in-the-loop - Alvaro Saurin & Jose M Navarro, Adobe

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Platform Engineering]]
- Temas: [[AI ML]], [[Platform Engineering]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Alvaro Saurin, Jose M Navarro, Adobe
- Schedule: https://kccnceu2026.sched.com/event/2CVyx/enterprise-scale-migrations-using-agentic-workflows-with-human-in-the-loop-alvaro-saurin-jose-m-navarro-adobe
- Busca YouTube: https://www.youtube.com/results?search_query=Enterprise-Scale+Migrations+Using+Agentic+Workflows+with+Human-in-the-loop+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Enterprise-Scale Migrations Using Agentic Workflows with Human-in-the-loop.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CVyx/enterprise-scale-migrations-using-agentic-workflows-with-human-in-the-loop-alvaro-saurin-jose-m-navarro-adobe
- YouTube search: https://www.youtube.com/results?search_query=Enterprise-Scale+Migrations+Using+Agentic+Workflows+with+Human-in-the-loop+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=m6jAXyS9_Ek
- YouTube title: Enterprise-Scale Migrations Using Agentic Workflows with Human-in... Alvaro Saurin & Jose M Navarro
- Match score: 0.901
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/enterprise-scale-migrations-using-agentic-workflows-with-human-in-the/m6jAXyS9_Ek.txt
- Transcript chars: 17747
- Keywords: gateway, traffic, translation, configuration, migration, running, agents, engineer, migrations, process, changes, correct, metrics, engineers, configurations, llm, produce, checking

### Resumo baseado na transcript

We are both senior software engineers in the gateway team in Adobe that is part of the developer platforms organization in the company. And today we are going to talk about an engineering problem that we have been trying to solve in in our team. And then uh we would grab and translate the old configuration and deploy the new configuration in Kubernetes with Argo CD and then Mboy would load that configuration those HTTP proxy resources that were deployed in Kubernetes. Let's look at the the problem and what we must do with these configurations. Erh but the first problem that when we found was that the translation between very different schemas was not easy for LLMs. So then we discarded this solution and we changed the approach to this problem.

### Excerpt da transcript

My name is Albert Saurin and my colleague is Jose Manuel Navaro. We are both senior software engineers in the gateway team in Adobe that is part of the developer platforms organization in the company. And today we are going to talk about an engineering problem that we have been trying to solve in in our team. It's the migration of an API gateway from engineext to to Mboy. So let's start by defining what an API gateway is. Um DNS is sending traffic for different services uh to the nodes of the API gateway and the API gateway then performs some vital things like authentication, authorization, uh routing, throttling or analytics and the traffic is uh sent to the different services that are running in this case in in Kubernetes. So the old gateway was based on engineext and Lua code for the business logic and the new gateway is based on more modern technologies like Envoy or Argo City. The migration presented multiple challenges. Erh the old gateway was u running for a long time but we would like to to benefit uh from newer technologies based on GitHubs and and to provide sales service to our users.

But the scale of this migration was breathtaking. um the complexity of the configurations being migrated involving 2600 services distributed in more than um 500 clusters each one with multiple environments made this a very complex migration and the goals we had were clear the migration should be transparent for users it could not require changes in the users configuration and failure failures were not possible possible because some of these services were really uh critical for for the company and cannot have any downtime. And just to give you some quick uh glimpse of the traffic managed by the old gateway uh 13 pabytes of traffic per month and 40 billion requests per day. So the approach uh was to try to migrate manually the services that were responsible for 80% of the traffic. uh that's not a very large number of services but uh we wanted to use some kind of automatic migrations for the rest of the traffic for the long tail of services right uh so we calculated that for doing this kind of migrations manually by engineers in an optimistic scenario that would require something like four years and a half but if things went south it could take 15 years.

So this is our manager and we decided that this was clearly impossible to do right in this way. So we found a solution. We would perform migrations of service services in autonomous way involving engineers only when
