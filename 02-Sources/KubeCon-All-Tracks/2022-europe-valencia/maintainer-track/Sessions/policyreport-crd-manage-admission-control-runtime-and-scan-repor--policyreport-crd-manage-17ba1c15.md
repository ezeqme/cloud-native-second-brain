---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Maintainer Track"
themes: ["AI ML", "Security", "Runtime Containers", "Community Governance"]
speakers: ["Anushka Mittal", "Mritunjay Sharma", "Nirmata", "Frank Jogeleit", "Lovoo GmbH", "Stephen Adeniyi"]
sched_url: https://kccnceu2022.sched.com/event/ytuV/policyreport-crd-manage-admission-control-runtime-and-scan-reports-anushka-mittal-mritunjay-sharma-nirmata-frank-jogeleit-lovoo-gmbh-stephen-adeniyi
youtube_search_url: https://www.youtube.com/results?search_query=PolicyReport+CRD%3A+Manage+Admission+Control%2C+Runtime%2C+and+Scan+Reports%21+CNCF+KubeCon+2022
slides: []
status: parsed
---

# PolicyReport CRD: Manage Admission Control, Runtime, and Scan Reports! - Anushka Mittal & Mritunjay Sharma, Nirmata; Frank Jogeleit, Lovoo GmbH; Stephen Adeniyi

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Runtime Containers]], [[Community Governance]]
- País/cidade: Spain / Valencia
- Speakers: Anushka Mittal, Mritunjay Sharma, Nirmata, Frank Jogeleit, Lovoo GmbH, Stephen Adeniyi
- Schedule: https://kccnceu2022.sched.com/event/ytuV/policyreport-crd-manage-admission-control-runtime-and-scan-reports-anushka-mittal-mritunjay-sharma-nirmata-frank-jogeleit-lovoo-gmbh-stephen-adeniyi
- Busca YouTube: https://www.youtube.com/results?search_query=PolicyReport+CRD%3A+Manage+Admission+Control%2C+Runtime%2C+and+Scan+Reports%21+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre PolicyReport CRD: Manage Admission Control, Runtime, and Scan Reports!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytuV/policyreport-crd-manage-admission-control-runtime-and-scan-reports-anushka-mittal-mritunjay-sharma-nirmata-frank-jogeleit-lovoo-gmbh-stephen-adeniyi
- YouTube search: https://www.youtube.com/results?search_query=PolicyReport+CRD%3A+Manage+Admission+Control%2C+Runtime%2C+and+Scan+Reports%21+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=tG-YLGF9_Aw
- YouTube title: PolicyReport CRD: Manage Admission Control, Runtime, and Scan Reports!
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/policyreport-crd-manage-admission-control-runtime-and-scan-reports/tG-YLGF9_Aw.txt
- Transcript chars: 24167
- Keywords: policy, report, adapter, cluster, results, reports, trivia, reporter, working, resource, policies, output, process, security, sidekick, mentioned, adapters, architecture

### Resumo baseado na transcript

hello everyone wow this is loud uh welcome to valencia welcome to the conference and welcome to hopefully the last session for today so yeah let's go yeah it's been an exhausting five days let's let's wrap this with a huge ban so today we will be talking about policy report crd and how you can manage your admission control runtime and scan reports and that's amazing so before we get into the technical part of the adapters and the policy reporters let's maybe go through a quick round of one problem was for me if you have a cluster-wide policy which violates namespace scoped resources you have many resources across many namespaces so it's very hard to find all results that relates to a single policy also you have the problem that a single

### Excerpt da transcript

hello everyone wow this is loud uh welcome to valencia welcome to the conference and welcome to hopefully the last session for today so yeah let's go yeah it's been an exhausting five days let's let's wrap this with a huge ban so today we will be talking about policy report crd and how you can manage your admission control runtime and scan reports and that's amazing so before we get into the technical part of the adapters and the policy reporters let's maybe go through a quick round of introduction so today we have four panelists one of us wasn't able to join us because of some visa issues that's stephen right there and we'll come to his introduction we have a video from him in a quick well i am anushka mithal i come from india i'm in my pre-final year pursuing bachelors in engineering i have worked with falco in the past i'll be talking about falco adapter soon i work with kiberno currently and let's go let's over to you yeah i'm frank i'm from germany i'm a senior software developer working at lavu and i'm also a contributor to different open source projects like farco and kyverno and yeah i'm also the maintainer of policy reporter which will i present in this talk so jay hi everyone welcome to our talk my name is brittan jay and i also belong from india currently i'm a finally a computer science engineering student of bachelor's in technology from india and i'm also an intern with nirmata currently i'm contributing to kyberno other than that previously last year i worked with jim bugwadia as a part of lfx mentorship to build cubans adapter which we are going to talk about in today's talk but before we move on to the adapters let's discuss what was the foundation and motivation behind the formation of uh policy working group anushka would you love to would you like to let us know about that yeah definitely so you know their policies are an important feature and we have earlier seen a lot of scattered support for policies on different levels of maturities so the purpose the motivation behind policy working group was basically to provide an overall architecture you know one platform to discuss current uh implementations of policy as well as discuss future implementations and future proposals so with this we were able to provide a universal view of policy architecture in kubernetes let's also talk about policy report crd this is what our adapters that we'll discuss in a while are based on so policy reports crd to tell you the motivation imagine having a hug
