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
speakers: ["Philip Conrad", "Maintainer"]
sched_url: https://kccncna2025.sched.com/event/27d4Z/project-lightning-talk-the-same-great-opa-only-faster-philip-conrad-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+The+Same+Great+OPA%2C+Only+Faster%21+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: The Same Great OPA, Only Faster! - Philip Conrad, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Philip Conrad, Maintainer
- Schedule: https://kccncna2025.sched.com/event/27d4Z/project-lightning-talk-the-same-great-opa-only-faster-philip-conrad-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+The+Same+Great+OPA%2C+Only+Faster%21+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: The Same Great OPA, Only Faster!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27d4Z/project-lightning-talk-the-same-great-opa-only-faster-philip-conrad-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+The+Same+Great+OPA%2C+Only+Faster%21+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=j-d3n88MZn4
- YouTube title: Project Lightning Talk: The Same Great OPA, Only Faster! - Philip Conrad, Maintainer
- Match score: 0.889
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-the-same-great-opa-only-faster/j-d3n88MZn4.txt
- Transcript chars: 4242
- Keywords: policy, version, improvements, slides, performance, engine, produces, policies, improving, indexer, everyone, colleague, sebastian, graduated, context, software, conditions, output

### Resumo baseado na transcript

My name is Philip Conrad and I'm one of the maintainers for the open policy agent project. Um, I'm presenting these slides on behalf of my colleague Sebastian who couldn't make it to CubeCon this year uh due to a family emergency. Uh, policies allow you to policies allow you to sorry um policies allow you to decouple a lot of your authorization logic from your applications and also allow checking for things like uh in the context of Kubernetes um do all of these containers come from a trusted registry. Um, and so we finally locked in a bunch of language changes that have been made and made a ton of performance improvements over the last year, mostly from doing uh, less work where we didn't need to be doing it. And my colleague Sebastian in version 1.3 contributed something that greatly improves the performance of generating decision logs which are very handy if you need to have audit logging for your open policy agent instances. We've continued this trend uh in the later part of the year uh with more improvements to the a compiler, improving the storage layer, and improving OPA's rule indexer.

### Excerpt da transcript

All right. Hello everyone. My name is Philip Conrad and I'm one of the maintainers for the open policy agent project. Um, I'm presenting these slides on behalf of my colleague Sebastian who couldn't make it to CubeCon this year uh due to a family emergency. So these are his slides but my words. Um, we'll be talking this year a little bit about OPA performance improvements. But if you don't know what OPA is, the open policy agent is a CNCF graduated project. Uh the project as a whole is about 10 years old and has been a CNCF graduated project for at least four years. Um folks tend to describe it as a general purpose policy engine. But what's a policy engine? Um, in the context of software, policy is sets of rules and conditions that determine the behavior of a piece of software. And an engine is something that takes an input and produces an output. When you combine these ideas, uh, you get something that takes an input, runs it through rules and conditions, and produces an output, which is what OPA does.

Um in the example on the slides behind me uh you can see that we have a user uh named Alice who has the admin role and we have a policy that checks to see is this person an admin and in this case they are and it produces true. Uh, policies allow you to policies allow you to sorry um policies allow you to decouple a lot of your authorization logic from your applications and also allow checking for things like uh in the context of Kubernetes um do all of these containers come from a trusted registry. This is a simple example but much more complex ones are possible. Over the last year, uh, we released a 1.0 version of the project. Um, up until literally the last year, uh, the project was just 0 whatever. Um, and so we finally locked in a bunch of language changes that have been made and made a ton of performance improvements over the last year, mostly from doing uh, less work where we didn't need to be doing it. uh fewer allocations on a lot of the hot pads and dramatically improving the efficiency of the abased interpreter.

Um in version 1.0 in particular, we started using sync.pool much more heavily if you're familiar with that from the Golang world. Uh this allows you to reuse applications you've already made and avoid thrashing the garbage collector. Uh we also in version 1.4 four dramatically improved the efficiency of several of the text handling built-ins. So, we make fewer allocations when we don't need to. And my colleague Sebastian in version 1.3 c
