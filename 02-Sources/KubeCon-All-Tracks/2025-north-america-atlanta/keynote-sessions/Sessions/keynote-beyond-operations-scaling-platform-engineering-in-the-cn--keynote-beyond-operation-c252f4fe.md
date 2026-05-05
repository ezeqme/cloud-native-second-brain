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
themes: ["Platform Engineering", "SRE Reliability", "Community Governance"]
speakers: ["Abby Bangser", "Principal Engineer", "Syntasso"]
sched_url: https://kccncna2025.sched.com/event/27dEm/keynote-beyond-operations-scaling-platform-engineering-in-the-cncf-community-abby-bangser-principal-engineer-syntasso
youtube_search_url: https://www.youtube.com/results?search_query=Keynote%3A+Beyond+Operations%3A+Scaling+Platform+Engineering+in+the+CNCF+Community+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Keynote: Beyond Operations: Scaling Platform Engineering in the CNCF Community - Abby Bangser, Principal Engineer, Syntasso

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[Platform Engineering]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Abby Bangser, Principal Engineer, Syntasso
- Schedule: https://kccncna2025.sched.com/event/27dEm/keynote-beyond-operations-scaling-platform-engineering-in-the-cncf-community-abby-bangser-principal-engineer-syntasso
- Busca YouTube: https://www.youtube.com/results?search_query=Keynote%3A+Beyond+Operations%3A+Scaling+Platform+Engineering+in+the+CNCF+Community+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Keynote: Beyond Operations: Scaling Platform Engineering in the CNCF Community.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27dEm/keynote-beyond-operations-scaling-platform-engineering-in-the-cncf-community-abby-bangser-principal-engineer-syntasso
- YouTube search: https://www.youtube.com/results?search_query=Keynote%3A+Beyond+Operations%3A+Scaling+Platform+Engineering+in+the+CNCF+Community+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=gmAfYEPBYr0
- YouTube title: Keynote: Beyond Operations: Scaling Platform Engineering in the CNCF Community - Abby Bangser
- Match score: 1.001
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/keynote-beyond-operations-scaling-platform-engineering-in-the-cncf-com/gmAfYEPBYr0.txt
- Transcript chars: 16526
- Keywords: platform, platforms, organization, organizations, internal, create, principles, engineering, business, software, across, support, started, deliver, infrastructure, ownership, safety, depend

### Resumo baseado na transcript

It's so nice to see some shining faces despite the sponsor parties last night. Maybe a few tired eyes, but it's so great that you all are here this morning because I want to talk about how software delivery changes and asks more of us each and every year. It's the same thing cloud providers gave us by removing the need to worry about power and physical security and cooling and allowed us to still have ownership over our infrastructure but in the demands of our organization. We have a challenge in one area like safety and we do something to make it better but then we create a problem in speed or efficiency and we just play this game over and over again and we wind up doing our best and each iteration does help but it also is reactive to the pain of the past iteration and it costs a lot to do the migrations to these new types of platforms. And of course, this is meant to bring in safety, but it's at the cost of agility and it ends up creating even some safety challenges, but it's still really prevalent today in platforms.

### Excerpt da transcript

Good morning everyone. It's so nice to see some shining faces despite the sponsor parties last night. Maybe a few tired eyes, but it's so great that you all are here this morning because I want to talk about how software delivery changes and asks more of us each and every year. 20 years ago, we got cloud computing that brought in infrastructure provisioning at a speed we had never seen before. 15 years ago, DevOps practices once again changed the game. 10 years ago, it is this community, cloudnative architectures and Kubernetes that once again shifted things. And if you've been here all week, you know that today it's AI. AI is once again changing the game of what is required of our internal platforms to support our organizations with innovation. So what I want to do today is share with you the new playbook for how platform engineering can prepare you, your organizations and your platforms for success with AI adoption. To get started, we have to start with why we even build platforms in the first place.

That is always what we have to return to. And it's we build them to reduce the scope and complexity for those that build on top of the platforms for the application teams that are trying to deliver business value to the end users of your organization. That is always has to be our focus. But the thing is is some people worry that this by building things into the platform we're removing autonomy and ownership from those that are delivering the applications. That's not the case. What we're doing is we're giving them focus. We're giving them the ability to do the things that matter to your organization and not have to worry about the dependencies that they require. It's the same thing cloud providers gave us by removing the need to worry about power and physical security and cooling and allowed us to still have ownership over our infrastructure but in the demands of our organization. Once we deliver these platforms or know what we need to deliver, we need to also measure their success. And in my experience, that means we're trying to balance how we can go faster, safer, and more efficiently all at the same time, which is a super simple job, right?

Despite the target always being balancing these three, the reality is that they're intention against each other. And so what ends up happening is as we build these internal platforms, we end up on a pendulum swing, or as I like to look at it, playing whack-a-ole. We have a challenge in one area like safety and we do
