---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Security"
themes: ["AI ML", "Security", "Platform Engineering"]
speakers: ["James Elías Sigurðarson", "Vignir Hafsteinsson", "Asana"]
sched_url: https://kccnceu2026.sched.com/event/2CW34/invisible-guardrails-enabling-developer-velocity-with-a-secure-platform-james-elias-sigurdarson-vignir-hafsteinsson-asana
youtube_search_url: https://www.youtube.com/results?search_query=Invisible+Guardrails%3A+Enabling+Developer+Velocity+With+a+Secure+Platform+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Invisible Guardrails: Enabling Developer Velocity With a Secure Platform - James Elías Sigurðarson & Vignir Hafsteinsson, Asana

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]], [[Platform Engineering]]
- País/cidade: Netherlands / Amsterdam
- Speakers: James Elías Sigurðarson, Vignir Hafsteinsson, Asana
- Schedule: https://kccnceu2026.sched.com/event/2CW34/invisible-guardrails-enabling-developer-velocity-with-a-secure-platform-james-elias-sigurdarson-vignir-hafsteinsson-asana
- Busca YouTube: https://www.youtube.com/results?search_query=Invisible+Guardrails%3A+Enabling+Developer+Velocity+With+a+Secure+Platform+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Invisible Guardrails: Enabling Developer Velocity With a Secure Platform.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW34/invisible-guardrails-enabling-developer-velocity-with-a-secure-platform-james-elias-sigurdarson-vignir-hafsteinsson-asana
- YouTube search: https://www.youtube.com/results?search_query=Invisible+Guardrails%3A+Enabling+Developer+Velocity+With+a+Secure+Platform+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=mxjiSCnrb3c
- YouTube title: Invisible Guardrails: Enabling Developer Velocity W... James Elías Sigurðarson & Vignir Hafsteinsson
- Match score: 0.783
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/invisible-guardrails-enabling-developer-velocity-with-a-secure-platfor/mxjiSCnrb3c.txt
- Transcript chars: 28777
- Keywords: security, application, permissions, platform, permission, policies, network, infrastructure, single, clusters, cluster, policy, allowed, developer, deployment, velocity, changes, needed

### Resumo baseado na transcript

James and I we work out of Asana's office in Reik Iceland where we uh yeah basically build weird infrastructure every day. Asana is a work management platform and Asana's mission at at Asana, our mission is to help humanity thrive by enabling the world's teams to work together effortlessly. We'll then dive deep into some of the security features we built into the platform and finally we'll share some of the lessons learned from our experience that will hopefully help you on your own journey. So at Aana uh security is our highest priority but for a long time we were forced to accept a difficult trade-off security versus velocity. Some investments we made in security came at the cost of developer velocity while other investments that were meant to increase both security and velocity often did not scale. At Asana, we started the Kubernetes journey in AWS many years ago by creating single tenant clusters which we called cube apps which were fully operated by the inf infrastructure teams which owned them.

### Excerpt da transcript

Hello and welcome to our talk. Uh my name is James and I'm an infrastructure engineer at Asana. >> And my name is Vign. I'm an engineering manager with one of the platform teams at Asana. James and I we work out of Asana's office in Reik Iceland where we uh yeah basically build weird infrastructure every day. Uh quick intro to our company. Asana is a work management platform and Asana's mission at at Asana, our mission is to help humanity thrive by enabling the world's teams to work together effortlessly. As such, the Asana product is trusted by over 170,000 organizations with millions of users that depend on Asana to get their work done every day. As such, we need to build infrastructure that is stable, performant, but most of all secure for those users. And our teams at the office have been responsible for building that infrastructure. Now today we want to tell you about our experience of building out an infrastructure platform with security as one of its first class features. We'll start out by sharing some of the historical problems we were facing and some of the difficult trade-offs we were making in favor of security.

Next, we'll discuss how escalating scaling issues presented us with an opportunity to entirely rethink our architecture, define some guiding principles that allowed us to reject some of those old trade-offs. We'll then dive deep into some of the security features we built into the platform and finally we'll share some of the lessons learned from our experience that will hopefully help you on your own journey. So at Aana uh security is our highest priority but for a long time we were forced to accept a difficult trade-off security versus velocity. Some investments we made in security came at the cost of developer velocity while other investments that were meant to increase both security and velocity often did not scale. At Asana, we started the Kubernetes journey in AWS many years ago by creating single tenant clusters which we called cube apps which were fully operated by the inf infrastructure teams which owned them. Our infrastructure security team could then treat each of these cube apps as a blackbox securing it externally using AWS IM roles and security groups all managed centrally by them.

Now this this did give our info teams autonomy but at the cost of control over their security. This model however this model broke as our infrastructure grew in size and we had more of these cube apps and teams owning them. Changes to security
