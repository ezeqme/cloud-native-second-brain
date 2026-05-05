---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Project Opportunities"
themes: ["AI ML", "Community Governance"]
speakers: ["Andres Aguiar", "Maintainer"]
sched_url: https://kccnceu2026.sched.com/event/2EFyl/project-lightning-talk-openfga-for-agents-safe-delegation-in-5-minutes-andres-aguiar-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+OpenFGA+For+Agents%3A+Safe+Delegation+In+5+Minutes+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: OpenFGA For Agents: Safe Delegation In 5 Minutes - Andres Aguiar, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Andres Aguiar, Maintainer
- Schedule: https://kccnceu2026.sched.com/event/2EFyl/project-lightning-talk-openfga-for-agents-safe-delegation-in-5-minutes-andres-aguiar-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+OpenFGA+For+Agents%3A+Safe+Delegation+In+5+Minutes+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: OpenFGA For Agents: Safe Delegation In 5 Minutes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFyl/project-lightning-talk-openfga-for-agents-safe-delegation-in-5-minutes-andres-aguiar-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+OpenFGA+For+Agents%3A+Safe+Delegation+In+5+Minutes+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=1_w_ZRJ5lWk
- YouTube title: Project Lightning Talk: OpenFGA For Agents: Safe Delegation In 5 Minutes - Andres Aguiar, Maintainer
- Match score: 0.928
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-openfga-for-agents-safe-delegation-in-5-minutes/1_w_ZRJ5lWk.txt
- Transcript chars: 6452
- Keywords: permissions, prompt, authorization, google, agents, presentation, access, control, credentials, message, specific, channel, linear, autonomous, interactive, maintainer, sedant, couldn

### Resumo baseado na transcript

Is inspired on some content that he created and I'm trying to represent those ideas. You're using it if you want to build authorization for an app or for an agentic app. This is a a performance a latency graph that was shared by the team at docker after there and migrated to the latest version. So I have a video now that what is doing is is going to is I have two uh two demos.

### Excerpt da transcript

So I'm Andreas. I'm an open HJ maintainer. Uh this presentation was submitted by Sedant. Sedant is a maintainer. He lives in India. He couldn't make it. So I'm doing the presentation for him. Is inspired on some content that he created and I'm trying to represent those ideas. So Open FGA is an authorization service for developers. You're using it if you want to build authorization for an app or for an agentic app. And it's inspired in the in a project by Google called Google Zanzibar. And we extend and which works with relationship based access control. You can see there's an evolution of role based access control and attribute based access control. Zanzibar in at Google P and the powers things like Google Google Docs or Google cloud or YouTube and uh so it's a build to scale to large RPS and and data volume. And what we did is we packaged those ideas with great developer tooling. and uh so you can use it for your own applications. These some of the adopters of OpenMGA. There's an adopters MD page where everyone can add themselves.

These are the companies they did. Thank you very much for all of them. There are big names there. And uh in the last six months since the last time we did this in in the US, we were adopted in accepted in incubation. So that's great news for the project. We just launched support for open zen 1.0 zero is an specification from open ID to how to do authorization checks and also we've been working a lot on performance. This is a a performance a latency graph that was shared by the team at docker after there and migrated to the latest version. So you'll see latency decreased a lot there. Let's talk about agents. I'm going to present here a solution for a use case with this constraints. First the agent needs to use credentials. Those credentials are going to have some permissions. They can be on behalf of a user, on behalf of uh service, I don't care. We want to restrict what agents can do on top of their API credentials. Okay? So less permissions than what they already have. Agents start with zero permissions and we run them ephemeral per task permissions.

Let's introduce a little of Open FGA. In Open FGA, you define what we call an authorization model where you declare the entities that are relevant when making authorization decisions. If we want to model something like MCP, this is a very simple way of doing it. We're going to have an entity that is a tool and then a parameter that we can specify on a tool and we can say that we
