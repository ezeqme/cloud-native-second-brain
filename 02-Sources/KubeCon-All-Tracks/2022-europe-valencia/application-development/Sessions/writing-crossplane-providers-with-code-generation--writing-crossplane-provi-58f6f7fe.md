---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Application + Development"
themes: ["Application + Development"]
speakers: ["Muvaffak Onuş", "Hasan Türken", "Upbound"]
sched_url: https://kccnceu2022.sched.com/event/ytrS/writing-crossplane-providers-with-code-generation-muvaffak-onus-hasan-turken-upbound
youtube_search_url: https://www.youtube.com/results?search_query=Writing+Crossplane+Providers+with+Code+Generation+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Writing Crossplane Providers with Code Generation - Muvaffak Onuş & Hasan Türken, Upbound

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Application + Development]]
- Temas: [[Application + Development]]
- País/cidade: Spain / Valencia
- Speakers: Muvaffak Onuş, Hasan Türken, Upbound
- Schedule: https://kccnceu2022.sched.com/event/ytrS/writing-crossplane-providers-with-code-generation-muvaffak-onus-hasan-turken-upbound
- Busca YouTube: https://www.youtube.com/results?search_query=Writing+Crossplane+Providers+with+Code+Generation+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Writing Crossplane Providers with Code Generation.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytrS/writing-crossplane-providers-with-code-generation-muvaffak-onus-hasan-turken-upbound
- YouTube search: https://www.youtube.com/results?search_query=Writing+Crossplane+Providers+with+Code+Generation+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=EN_vqJivZrk
- YouTube title: Writing Crossplane Providers with Code Generation - Muvaffak Onuş & Hasan Türken, Upbound
- Match score: 0.822
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/writing-crossplane-providers-with-code-generation/EN_vqJivZrk.txt
- Transcript chars: 55580
- Keywords: database, provider, create, password, resource, external, planet, cluster, composition, controller, crossplane, secret, implement, resources, fields, organization, providers, delete

### Resumo baseado na transcript

um it's a tutorial form uh so we're gonna like you know hands-on develop a crossband provider which is like you know a set of kubernetes controllers with their own crds so uh before starting how many uh like hands up if you have been using cross playing with like you know other providers right now nice uh so how many of you just heard crossplane but not using it yet or just like you know at the consideration phase nice and how many of you started actually developing provider

### Excerpt da transcript

um it's a tutorial form uh so we're gonna like you know hands-on develop a crossband provider which is like you know a set of kubernetes controllers with their own crds so uh before starting how many uh like hands up if you have been using cross playing with like you know other providers right now nice uh so how many of you just heard crossplane but not using it yet or just like you know at the consideration phase nice and how many of you started actually developing provider and like you know got stuck somewhere so you're looking like how to develop that yeah cool all right cool um so yeah writing cross pain providers so cross paying providers allow you to bring any external resource external api into your cluster as is as crds so this is not like you know really like a unknown or like a very novel thing but like you know with the tools and runtime and code generation tooling we built we have now a framework optimized for interacting with crud external resource apis for for example like you know the main thing with the kubernetes control is like apply logic like hey update if it already exists and like you know create only if it doesn't et cetera so like all these are like you know handled uh towards like you know optimus optimized for assuming that the external api is like you know uh in design in corrupt method not like in a declarative fashion so essentially what we do here like you know have a framework that contains like you know runtime and code generation tooling that will allow you to take an imperative api and expose it as declarative api and use cross-plain primitives abstractions and compositions on top of it so yeah a little bit up about us so i'm well [ __ ] uh i work at that pound and i make i've been a crosstalk maintainer since v 0.3 which is around like three years now and i had worked at sap before that again developing kubernetes controllers in sun yeah i'm hasan and just like [ __ ] i'm working at upbound and i am the newest maintainer of crossplane uh with crossplane 1.7 release we shipped the external secret store feature and after that uh i am honored to be a uh crossband maintainer yeah and there are lots of like you know provider maintainers which are like you know on the orders of 10 so feel free to like after this tutorial feel free to go ahead and contribute and like you know become a maintainer cool so we can we can start so what is a cross pin provider as i just mentioned just like you create pods and deployment resources cros
