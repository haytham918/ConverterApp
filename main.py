from units import *
from currency import *
from times import *
import flexx
from flexx import flx
import os


# CERTFILE = '/tmp/self-signed.crt'
# KEYFILE = '/tmp/self-signed.key'

# os.system('openssl req -x509 -nodes -days 1 -batch -newkey rsa:2048 '
#           '-keyout %s -out %s' % (KEYFILE, CERTFILE))

# use the self-signed certificate as if specified in normal config
# flx.config.ssl_certfile = CERTFILE
# flx.config.ssl_keyfile = KEYFILE

flx.config.port = os.environ.get('PORT', '5000')


class Units(flx.PyWidget):
    CSS = """
    .flx-LineEdit {
        border: 2px solid #9d9;
    }

    .flx-Button {
        background : #007bff;
        color : white
    }

    .flx-ComboBox {
        border : 2px solid #2ec5d6
    }
    """

    def init(self):
        with flx.VBox():
            with flx.HBox():
                flx.Widget(flex=1)
                self.kind = flx.ComboBox(options=list(unit_kind.keys()))
                flx.Widget(flex=3)
                flx.Widget(flex=3)

            with flx.HBox():
                self.value_input = flx.LineEdit(placeholder_text="Value")
                self.before = flx.ComboBox()
                self.equal_sign = flx.Label(text="=")
                self.get_value = flx.LineEdit()
                self.after = flx.ComboBox()
            with flx.HBox():
                flx.Widget(flex=1)
                self.formula_ratio = flx.LineEdit(
                    placeholder_text="Ratio/Formula")
                flx.Widget(flex=1)

    @flx.reaction("kind.user_selected")
    def optionSelected(self, *events):
        event = events[-1]
        self.before.set_options(list(unit_kind[event.text].keys()))
        self.after.set_options(list(unit_kind[event.text].keys()))
        if self.formula_ratio != "":
            self.formula_ratio.set_text("")

    @flx.reaction("before.user_selected")
    def choose_before(self, *events):
        event = events[-1]
        temp = list(self.before.options[:])
        temp.remove(temp[event.index])
        self.after.set_options(temp)
        if self.formula_ratio != "":
            self.formula_ratio.set_text("")
        should_work = check_unit(self.kind.text, event.text, self.after.text,
                                 self.value_input.text)
        if should_work:
            if self.kind.selected_index == 12:
                f_v = temperature(
                    float(self.value_input.text), event.text, self.after.text)
                self.formula_ratio.set_text(f_v["formula"])
                self.get_value.set_text(str(f_v["value_after"]))
            else:
                f_v = units(unit_kind[self.kind.text],
                            float(self.value_input.text), event.text,
                            self.after.text)
                self.formula_ratio.set_text(str(f_v["formula"]))
                self.get_value.set_text(str(f_v["value_after"]))

    @flx.reaction("after.user_selected")
    def choose_after(self, *events):
        event = events[-1]
        if self.formula_ratio != "":
            self.formula_ratio.set_text("")
        should_work = check_unit(self.kind.text, self.before.text, event.text,
                                 self.value_input.text)
        if should_work:
            if self.kind.selected_index == 12:
                f_v = temperature(
                    float(self.value_input.text), self.before.text, event.text)
                self.formula_ratio.set_text(f_v["formula"])
                self.get_value.set_text(str(f_v["value_after"]))
            else:
                f_v = units(unit_kind[self.kind.text],
                            float(self.value_input.text), self.before.text,
                            event.text)
                self.formula_ratio.set_text(str(f_v["formula"]))
                self.get_value.set_text(str(f_v["value_after"]))

    @flx.reaction("value_input.user_text")
    def convert(self, *events):
        event = events[-1]
        if event.new_value == "":
            self.get_value.set_text("")
        should_work = check_unit(self.kind.text, self.before.text,
                                 self.after.text, event.new_value)
        if should_work:
            if self.kind.selected_index == 12:
                f_v = temperature(
                    float(event.new_value), self.before.text, self.after.text)
                self.formula_ratio.set_text(f_v["formula"])
                self.get_value.set_text(str(f_v["value_after"]))
            else:
                f_v = units(unit_kind[self.kind.text], float(event.new_value),
                            self.before.text, self.after.text)
                self.formula_ratio.set_text(str(f_v["formula"]))
                self.get_value.set_text(str(f_v["value_after"]))


class Currency(flx.PyWidget):
    CSS = """
    .flx-LineEdit {
        border: 2px solid #9d9;
    }
    .flx-Button {
        background : #007bff;
        color : white
    }
    .flx-ComboBox {
        border : 2px solid #2ec5d6
    }
    """

    def init(self):
        with flx.VBox():
            with flx.HBox():
                self.amount_input = flx.LineEdit(placeholder_text="Amount")
                self.former = flx.ComboBox(
                    options=list(options_currency.keys()))
                self.image1 = flx.ImageWidget(flex=5)
                self.equal_sign = flx.Label(text="=")
                self.amount_get = flx.LineEdit()
                self.latter = flx.ComboBox(
                    options=list(options_currency.keys()))
                self.image2 = flx.ImageWidget(flex=5)
            with flx.HBox():
                flx.Widget(flex=1)
                self.rate = flx.LineEdit(placeholder_text="Rate")
                flx.Widget(flex=1)

    @flx.reaction("former.user_selected")
    def choose_from(self, *events):
        event = events[-1]
        temp2 = list(self.former.options[:])
        temp2.remove(temp2[event.index])
        self.latter.set_options(temp2)
        choose_flag(self.image1, event.text[:3].lower())
        if self.rate.text != "":
            self.rate.set_text("")
        is_work = check_currency(event.text, self.latter.text,
                                 self.amount_input.text)
        if is_work:
            r_a = currency_conversion(options_currency[event.text],
                                      options_currency[self.latter.text],
                                      int(self.amount_input.text))
            self.rate.set_text(r_a["Rate"])
            self.amount_get.set_text(str(r_a["Amount"]))

    @flx.reaction("latter.user_selected")
    def choose_latter(self, *events):
        event = events[-1]
        choose_flag(self.image2, event.text[:3].lower())
        if self.rate.text != "":
            self.rate.set_text("")
        is_work = check_currency(self.former.text, event.text,
                                 self.amount_input.text)
        if is_work:
            r_a = currency_conversion(options_currency[self.former.text],
                                      options_currency[event.text],
                                      float(self.amount_input.text))
            self.rate.set_text(r_a["Rate"])
            self.amount_get.set_text(str(r_a["Amount"]))

    @flx.reaction("amount_input.user_text")
    def convert_money(self, *events):
        event = events[-1]
        if event.new_value == "":
            self.amount_get.set_text("")
        is_work = check_currency(self.former.text, self.latter.text,
                                 event.new_value)
        if is_work:
            r_a = currency_conversion(options_currency[self.former.text],
                                      options_currency[self.latter.text],
                                      float(event.new_value))
            self.rate.set_text(r_a["Rate"])
            self.amount_get.set_text(str(r_a["Amount"]))


class Time(flx.PyWidget):
    CSS = """
    .flx-LineEdit {
        border: 2px solid #9d9 !important;
    }
    .flx-Button {
        background : #007bff !important;
        color : white !important
    }
    .flx-ComboBox {
        border : 2px solid #2ec5d6 !important
    }
    """

    def init(self):
        with flx.VBox():
            with flx.HBox():
                flx.Widget(flex=1)
                self.get_nowtime = flx.Button(
                    minsize=40, text="Get your current time")
                self.current_time = flx.LineEdit(flex=1)
                flx.Widget(flex=1)
            with flx.HBox():
                flx.Widget(flex=1)
                self.kind_chosen = flx.ComboBox(options=list(category.keys()))
                self.continent_ocean = flx.ComboBox()
                self.spe_location = flx.ComboBox()
                self.enter_button = flx.Button(minsize=40, text="Enter")
                self.chosen_time = flx.LineEdit(flex=1)
                flx.Widget(flex=1)
            with flx.HBox():
                self.chosen_year = flx.ComboBox(options=the_year)
                self.chosen_month = flx.ComboBox(options=the_month)
                self.chosen_date = flx.ComboBox()
                self.chosen_hour = flx.LineEdit(
                    placeholder_text="Hour/24-hour-time")
                self.chosen_minute = flx.LineEdit(placeholder_text="Minute")
                self.before_area = flx.ComboBox(
                    options=list(select_timezone.keys()))
                self.before_location = flx.ComboBox()
                self.equal = flx.Label(text="=")
                self.result = flx.LineEdit()
                self.after_area = flx.ComboBox(
                    options=list(select_timezone.keys()))
                self.after_location = flx.ComboBox()

    @flx.reaction("get_nowtime.pointer_click")
    def printTime(self, *events):
        self.current_time.set_text(str(IPtime_now))

    @flx.reaction("kind_chosen.user_selected")
    def choose_area(self, *events):
        event = events[-1]
        if event.index == 0:
            self.continent_ocean.set_options(list(select_timezone.keys()))
        if event.index == 1:
            self.continent_ocean.set_options(Others)
            self.spe_location.set_selected_index(-1)
            self.spe_location.set_options(noneOptions)

    @flx.reaction("continent_ocean.user_selected")
    def choose_location(self, *events):
        event = events[-1]
        if self.kind_chosen.selected_index == 0:
            self.spe_location.set_options(select_timezone[event.text])
        if self.kind_chosen.selected_index == 1:
            self.spe_location.set_selected_index(-1)
            self.spe_location.set_options(noneOptions)

    @flx.reaction("enter_button.pointer_click")
    def get_the_time(self, *events):
        if self.kind_chosen.selected_index == 0:
            the_time = current_time(self.continent_ocean.text,
                                    self.spe_location.text)
        if self.kind_chosen.selected_index == 1:
            the_time = current_time_Special(self.continent_ocean.text)
        self.chosen_time.set_text(the_time)

    @flx.reaction("chosen_year.user_selected")
    def day_range(self, *events):
        event = events[-1]
        if self.chosen_month.text != "":
            range_date = daterange(
                int(event.text), int(self.chosen_month.text))
            self.chosen_date.set_options(range_date)
        whether_work = check_whether_work(
            event.text, self.chosen_month.text, self.chosen_date.text,
            self.chosen_hour.text, self.chosen_minute.text,
            self.before_area.text, self.before_location.text,
            self.after_area.text, self.after_location.text)
        if whether_work:
            time_value = time_conversion(
                int(event.text), int(self.chosen_month.text),
                int(self.chosen_date.text), int(self.chosen_hour.text),
                int(self.chosen_minute.text), self.before_area.text,
                self.before_location.text, self.after_area.text,
                self.after_location.text)
            self.result.set_text(str(time_value))

    @flx.reaction("chosen_month.user_selected")
    def monthchoose(self, *events):
        event = events[-1]
        if self.chosen_year.text != "":
            range_date = daterange(int(self.chosen_year.text), int(event.text))
            self.chosen_date.set_options(range_date)
        whether_work = check_whether_work(
            self.chosen_year.text, event.text, self.chosen_date.text,
            self.chosen_hour.text, self.chosen_minute.text,
            self.before_area.text, self.before_location.text,
            self.after_area.text, self.after_location.text)
        if whether_work:
            time_value = time_conversion(
                int(self.chosen_year.text), int(event.text),
                int(self.chosen_date.text), int(self.chosen_hour.text),
                int(self.chosen_minute.text), self.before_area.text,
                self.before_location.text, self.after_area.text,
                self.after_location.text)
            self.result.set_text(str(time_value))

    @flx.reaction("chosen_date.user_selected")
    def calculation5(self, *events):
        event = events[-1]
        whether_work = check_whether_work(
            self.chosen_year.text, self.chosen_month.text, event.text,
            self.chosen_hour.text, self.chosen_minute.text,
            self.before_area.text, self.before_location.text,
            self.after_area.text, self.after_location.text)
        if whether_work:
            time_value = time_conversion(
                int(self.chosen_year.text), int(self.chosen_month.text),
                int(event.text), int(self.chosen_hour.text),
                int(self.chosen_minute.text), self.before_area.text,
                self.before_location.text, self.after_area.text,
                self.after_location.text)
            self.result.set_text(str(time_value))

    @flx.reaction("before_area.user_selected")
    def choose_before_location(self, *events):
        event = events[-1]
        self.before_location.set_options(select_timezone[event.text])
        whether_work = check_whether_work(
            self.chosen_year.text, self.chosen_month.text,
            self.chosen_date.text, self.chosen_hour.text,
            self.chosen_minute.text, event.text, self.before_location.text,
            self.after_area.text, self.after_location.text)
        if whether_work:
            time_value = time_conversion(
                int(self.chosen_year.text), int(self.chosen_month.text),
                int(self.chosen_date.text), int(self.chosen_hour.text),
                int(self.chosen_minute.text), event.text,
                self.before_location.text, self.after_area.text,
                self.after_location.text)
            self.result.set_text(str(time_value))

    @flx.reaction("after_area.user_selected")
    def choose_after_location(self, *events):
        event = events[-1]
        self.after_location.set_options(select_timezone[event.text])
        whether_work = check_whether_work(
            self.chosen_year.text, self.chosen_month.text,
            self.chosen_date.text, self.chosen_hour.text,
            self.chosen_minute.text, self.before_area.text,
            self.before_location.text, event.text, self.after_location.text)
        if whether_work:
            time_value = time_conversion(
                int(self.chosen_year.text), int(self.chosen_month.text),
                int(self.chosen_date.text), int(self.chosen_hour.text),
                int(self.chosen_minute.text), self.before_area.text,
                self.before_location.text, event.text,
                self.after_location.text)
            self.result.set_text(str(time_value))

    @flx.reaction("chosen_hour.user_text")
    def calculation1(self, *events):
        event = events[-1]
        if event.new_value == "":
            self.result.set_text("")
        whether_work = check_whether_work(
            self.chosen_year.text, self.chosen_month.text,
            self.chosen_date.text, event.new_value, self.chosen_minute.text,
            self.before_area.text, self.before_location.text,
            self.after_area.text, self.after_location.text)
        if whether_work:
            time_value = time_conversion(
                int(self.chosen_year.text), int(self.chosen_month.text),
                int(self.chosen_date.text), int(event.new_value),
                int(self.chosen_minute.text), self.before_area.text,
                self.before_location.text, self.after_area.text,
                self.after_location.text)
            self.result.set_text(str(time_value))

    @flx.reaction("chosen_minute.user_text")
    def calculation2(self, *events):
        event = events[-1]
        if event.new_value == "":
            self.result.set_text("")
        whether_work = check_whether_work(
            self.chosen_year.text, self.chosen_month.text,
            self.chosen_date.text, self.chosen_hour.text, event.new_value,
            self.before_area.text, self.before_location.text,
            self.after_area.text, self.after_location.text)
        if whether_work:
            time_value = time_conversion(
                int(self.chosen_year.text), int(self.chosen_month.text),
                int(self.chosen_date.text), int(self.chosen_hour.text),
                int(event.new_value), self.before_area.text,
                self.before_location.text, self.after_area.text,
                self.after_location.text)
            self.result.set_text(str(time_value))

    @flx.reaction("before_location.user_selected")
    def calculation3(self, *events):
        event = events[-1]
        whether_work = check_whether_work(
            self.chosen_year.text, self.chosen_month.text,
            self.chosen_date.text, self.chosen_hour.text,
            self.chosen_minute.text, self.before_area.text, event.text,
            self.after_area.text, self.after_location.text)
        if whether_work:
            time_value = time_conversion(
                int(self.chosen_year.text), int(self.chosen_month.text),
                int(self.chosen_date.text), int(self.chosen_hour.text),
                int(self.chosen_minute.text), self.before_area.text,
                event.text, self.after_area.text, self.after_location.text)
            self.result.set_text(str(time_value))

    @flx.reaction("after_location.user_selected")
    def calculation4(self, *events):
        event = events[-1]
        whether_work = check_whether_work(
            self.chosen_year.text, self.chosen_month.text,
            self.chosen_date.text, self.chosen_hour.text,
            self.chosen_minute.text, self.before_area.text,
            self.before_location.text, self.after_area.text, event.text)
        if whether_work:
            time_value = time_conversion(
                int(self.chosen_year.text), int(self.chosen_month.text),
                int(self.chosen_date.text), int(self.chosen_hour.text),
                int(self.chosen_minute.text), self.before_area.text,
                self.before_location.text, self.after_area.text, event.text)
            self.result.set_text(str(time_value))


class Converter(flx.PyWidget):
    def init(self):
        with flx.TabLayout():
            Units(title="Units")
            Currency(title="Currency")
            Time(title="Time")


# app = flx.App(Converter)
# app = flx.App(Units)
# app.export('example.html', link=0)
if __name__ == "__main__":
    flx.serve(Converter, 'Converter')  # show it now in a browser
    flx.start()

