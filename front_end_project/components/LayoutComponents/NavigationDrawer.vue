<template>
  <v-navigation-drawer
    v-model="drawerFlag"
    class="overflow-hidden nav-bar"
    :width="mini ? '20%' : ''"
    dark
    hide-overlay
    dense
    v-bind:temporary="mini ? true : false"
    v-bind:permanent="mini ? false : true"
    v-bind:absolute="mini ? true : false"
    v-click-outside="hideDrawer"
  >
    <!-- <div class="title-icon">Fukakachi</div>-->
    <v-list>
      <v-list-item class="ml-10">
        <v-list-item-content>
          <v-list-item-title class="title-icon" v-on:click="openLink">
            {{ $t("Abnormal Action Dataset") }}
          </v-list-item-title>
          <v-list-item-subtitle>
            {{ $t("HUST 's System") }}
          </v-list-item-subtitle>
        </v-list-item-content>
        <v-btn icon v-on:click="hideDrawerButton" class="back-icon" v-if="mini">
          <v-icon>mdi-arrow-left</v-icon>
        </v-btn>
      </v-list-item>
      <v-list-item
        v-for="([icon, text, url], i) in items"
        v-on:click="hideDrawer"
        :key="i"
        link
        :to="url"
      >
        <v-list-item-icon class="list-icon">
          <v-icon>{{ icon }}</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>{{ text }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-item v-on:click="logout">
        <v-list-item-icon class="list-icon">
          <v-icon>mdi-logout-variant</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>{{ $t("LOGOUT") }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>
<style lang="scss" scoped>
.nav-bar {
  background-color: $accent-color !important;
}
.back-icon {
  margin: 1em;
}
.setting-list {
  margin-top: auto;
}
.title-icon {
  text-align: left;
  padding-top: 1rem;
  padding-bottom: 1rem;
  font-size: 2rem;
  font-weight: 600;
  cursor: pointer;
}
.list-icon {
  padding-left: 4px;
}
</style>
<script>
export default {
  created() {
    this.drawerFlag = false;
    let isDev = this.getCookie("isDev");

    if (isDev == "true") {
      this.items = [
        ["mdi-home", this.$t("Home"), this.localePath("/")],
        ["mdi-folder", this.$t("Datasets"), this.localePath("/DataSet")],
        [
          "mdi-account-circle",
          this.$t("Features"),
          this.localePath("/Personal")
        ],
        [
          "mdi-cog",
          this.$t("Account Setting"),
          this.localePath("/AccountSetting")
        ]
      ];
    } else {
      this.items = [
        ["mdi-home", this.$t("Home"), this.localePath("/")],
        ["mdi-folder", this.$t("Data Set"), this.localePath("/DataSet")],
        [
          "mdi-cog",
          this.$t("Account Setting"),
          this.localePath("/AccountSetting")
        ]
      ];
    }
  },
  props: {
    drawer: {
      type: Boolean,
      default: false
    }
  },
  watch: {
    mini: function(val, oldVal) {
      this.resetDrawer();
    }
  },
  computed: {
    drawerFlag: {
      // getter
      get: function() {
        return this.drawer;
      },
      // setter
      set: function(newValue) {
        return this.drawer;
      }
    },
    isAdmin() {
      return true;
    },
    mini() {
      switch (this.$vuetify.breakpoint.name) {
        case "xs":
          return true;
        case "sm":
          return true;
        case "md":
          return true;
        case "lg":
          return false;
        case "xl":
          return false;
      }
    }
  },
  data: () => ({
    items: []
  }),
  methods: {
    logout() {
      var me = this;
      this.$emit("logout");
    },
    openLink() {
      var me = this;
      me.$nuxt.$router.push({ path: this.localePath("/") });
    },
    resetDrawer() {
      this.$emit("reset-drawer");
    },
    hideDrawer() {
      if (!this.drawer) {
        this.$emit("hide-drawer");
      }
    },
    hideDrawerButton() {
      this.$emit("hide-drawer");
    },
    transitionend() {}
  }
};
</script>
