
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue') }
    ]
  },
  {
    path: '/cart',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Cart.vue') }
    ]
  },
  {
    path: '/wishlist',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/WishList.vue') }
    ]
  },
  {
    path: '/shop/:slug',
    params: 'slug',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Shop.vue') }
    ]
  },
  {
    path: '/label/:slug',
    params: 'slug',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/LabelDetail.vue') }
    ]
  },
  {
    path: '/brand/:slug',
    params: 'slug',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/BrandDetail.vue') }
    ]
  },
  {
    path: '/product/:id',
    params: 'id',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/posProductDetail.vue') }
    ]
  },
  {
    path: '/thanks/:slug',
    params: 'slug',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Thanks.vue') }
    ]
  },
  {
    path: '/privacy_policy',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/PrivacyPolicy') }
    ]
  },
  {
    path: '/info/:slug',
    params: 'slug',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/InfoPage.vue') }
    ]
  },
  {
    path: '/contacts',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Contacts.vue') }
    ]
  },
  {
    path: '/about',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/About.vue') }
    ]
  },
  {
    path: '/questions',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Questions.vue') }
    ]
  },
  {
    path: '/search',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/SearchPage.vue') }
    ]
  },
  {
    path: '/files',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Files.vue') }
    ]
  },
  {
    path: '/services',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Services/AllServices') }
    ]
  },
  {
    path: '/service_category/:slug',
    params: 'slug',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Services/ServiceCategoryDetail') }
    ]
  },
  {
    path: '/service/:id',
    params: 'id',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Services/ServiceDetail') }
    ]
  },


  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
